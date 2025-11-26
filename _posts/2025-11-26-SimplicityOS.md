---
layout: post
comments: true
title: Building a 64-bit OS from Scratch with Claude Code
image: /assets/posts/SimplicityOS.png
tags: [Technology, Programming, AI, Forth, Operating Systems]
---

It's getting cold in Oslo. Had a dinner with the boss two days ago, should
have been dressed better for the biting cold. Instead I got a cold. With fever
today and a stand-up meeting from bed, I wasn't much for work.

So I decided to build a bootable 64-bit operating system from absolute scratch in a single session. A real x86_64 OS with a working Forth interpreter using Claude Code.

My Assembly skills are rusty and from the coconut processor, so I'm glad I had
Claude to do the work here.

Here's how it went.

## The Spark

I asked Claude Code to help me build "Simplicity OS" - an operating system where everything is a Forth word. The entire OS would be like Lego blocks: simple, composable words that directly control hardware. Want to know your screen resolution? `SCREEN` returns all parameters to the stack. Want to change brightness? `SCREEN-SET` takes parameters from the stack and applies them.

Pure, simple & direct.

## The Request

Near the end of our session, I asked Claude:

```
Now, before we get into the more involved stuff, can you create a file "MakingAnOS.md"
where you write all my prompts from start to finish here with your responses (no need to
include all the code changes etc since that will make the file huge). The purpose here is
to showcase what can be done with Claude Code [Sonnet 4.5 (1M context)] from scratch -
with full transparency and basically remove any bragging rights pointing back at me. I
want to show other developers what they can do.
```

Claude created that document. You can [read the complete session narrative here](/assets/posts/MakingAnOS.md) - every prompt, every response, every challenge, every breakthrough.

## What We Built

**In roughly 2 hours, from an empty directory:**

- Complete project structure with Makefiles, git hooks, documentation
- 512-byte boot sector (16-bit real mode)
- Stage2 bootloader with full CPU mode progression
- 64-bit long mode (x86_64) working
- Forth interpreter with NEXT execution loop
- 14 working Forth words
- VGA text output
- String and number printing
- All in 1,351 bytes of bootable code

**It actually works.** You can clone the repo, run `make run`, and watch it boot in QEMU.

## The Journey

### Stage 0: Protected Mode (30 minutes)

Got the boot sector loading, stage2 entering 32-bit protected mode, and displaying hardcoded arithmetic. First "hello world" moment when we saw:

```
Simplicity OS v0.1 - Protected mode
5 35
```

### Stage 1: Forth Interpreter (45 minutes)

Built a real Forth interpreter with the NEXT inner loop. Hit a critical bug - used `jmp [eax]` (double dereference) instead of `jmp eax`. Debugged with markers, found the issue, fixed it.

Suddenly we had Forth code executing:
```forth
2 3 + .    → prints "5"
5 7 * .    → prints "35"
```

### The 64-bit Wall (1 hour)

Tried to add 64-bit long mode. Failed. Tried different page table locations (0x1000, 0x10000, 0x70000, 0x9000). All crashed. System would triple-fault and reboot.

Documented all failures. Recommended staying in 32-bit.

### The Breakthrough (30 minutes)

I asked: "Can we get that long mode 64-bit to work with some ultrathink?"

Claude found it. The issue: **you can't use a 64-bit GDT while executing 32-bit code.**

The solution:
1. Use 32-bit GDT during setup
2. Enable long mode while in 32-bit code
3. Load a NEW 64-bit GDT after long mode is active
4. Far jump to 64-bit code segment

Added debug markers: P-C-A-E-L

When I saw "PCAE" in red and "L64" in yellow, we had it. **64-bit code was executing.**

## What This Shows

This isn't about me being clever. I gave vision and direction. Claude did the heavy lifting:

- Wrote all the assembly code
- Debugged boot issues
- Handled build systems (Make, NASM, QEMU)
- Managed git commits
- Found the 64-bit solution after multiple failures
- Created all documentation

**The complete development narrative is transparent.** Read [MakingAnOS.md](/assets/posts/MakingAnOS.md) - every prompt, every response, every struggle. Nothing hidden. No cherry-picking. This is what actual development with Claude Code looks like.

## Technical Highlights

**The NEXT Loop** (heart of Forth):
```asm
NEXT:
    lodsq       ; Load next word address (64-bit)
    jmp rax     ; Execute it
```

**The 64-bit Solution** (two-GDT approach):
```asm
; Setup in 32-bit code
mov cr0, eax            ; Enable long mode
lgdt [gdt64_descriptor] ; Load 64-bit GDT
jmp 0x08:long_mode_64   ; Jump to 64-bit segment

[BITS 64]
long_mode_64:
    ; Now executing 64-bit code!
```

**Current Forth Words** (14 total):
- Stack: DUP DROP SWAP ROT OVER
- Arithmetic: + - * /
- Memory: @ !
- I/O: . (numbers) QUOTE (strings)
- Control: LIT BYE

## Why Forth?

Forth is perfect for OS work:
- Minimal implementation (NEXT loop + dictionary)
- Self-hosting and extensible
- Direct hardware access
- Interactive development (REPL)
- Everything is composable

The entire OS will be Forth words. Want to read from disk? `DISK-READ`. Want to set screen brightness? `SCREEN-SET`. Everything follows the same pattern.

## What's Next

The OS is just beginning:
- Keyboard input (PS/2 driver)
- Interactive REPL (type Forth code live)
- Colon definitions (compile new words)
- Disk I/O
- More drivers following the DEVICE-* convention

All development will be transparent. All code public domain.

## For Other Developers

If you're wondering what Claude Code can do:

**Read the full narrative**: [MakingAnOS.md](/assets/posts/MakingAnOS.md)

You'll see:
- The actual conversation flow
- Design decisions and rationale
- Failed attempts and debugging
- The breakthrough moment
- What works, what doesn't, why

**Try it yourself**:
```bash
git clone https://github.com/isene/SimplicityOS
cd SimplicityOS
make run
```

- Read the code
- Build on it
- See what you can create with Claude Code

This is reproducible. The tools are available. The AI is accessible.

## Going Forward

I'm creating the [Simplicity OS](https://github.com/isene/SimplicityOS) to have something to tinker with. Having built
a programming language ([XRPN](https://github.com/isene/XRPN)), a shell ([rsh](https://github.com/isene/rsh)), a curses library ([rcurses](https://github.com/isene/rcurses)), a
file manager ([RTFM](https://github.com/isene/RTFM)) and other tools I have enjoyed tinkering with, I needed
something new to nerd out on.

---

## Transparency

This post was written by Claude Code based on our actual development session. The narrative document was also created by Claude. All code is public domain.

The point: Show what's possible. No gatekeeping. No mystery. Just: "Here's what we did, here's how we did it, go build something."

---

![Simplicity OS](/assets/posts/SimplicityOS.png)

*Simplicity OS v0.2 running in QEMU - 64-bit Forth interpreter executing: "Test" 2 3 + .*

---
Link to this post: <https://isene.org/2025/11/SimplicityOS.html>
