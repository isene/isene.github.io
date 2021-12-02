---
layout: post
title: HyperList
permalink: /hyperlist/
---

![](/assets/img/hyperlist.png)

### Everything. Concise and precise.
HyperListS represents a way to describe anything – any state or any transition. It represents data in tree-structure lists with a very rich set of features. It can be used for any structuring of data, such as:

- Todo lists
- Project plans
- Data structures
- Business processes
- Logic breakdowns
- Food recipes
- Outlines of ideas
- . . . and much, much more

Read this OnePagePook to get a primer on HyperLists:

<img src="/assets/onepagebooks/7-hyperlist/cover.jpg" width="500"><br />
**[Downloadable PDF](/assets/onepagebooks/7-hyperlist/1PB_HyperList.pdf)**

> The list is the origin of culture. It’s part of the history of art and literature. What does culture want? To make infinity comprehensible. It also wants to create order – not always, but often. And how, as a human being, does one face infinity? How does one attempt to grasp the incomprehensible? Through lists (Umberto Eco)

#### HyperList document
For an in-depth explanation of all the possibilities HyperList can give, get the <a href="/assets/files/hyperlist.pdf" target="_blank" rel="noopener">HyperList document</a> (PDF).

#### VIM plugin
To facilitate the creation and managing of HyperListS, I have created an elaborate plugin for the VIM text editor.

Check out this screencast for a short intoduction to some main features (view in HD):

{% include youtube.html id='xVUPJQhOBiU' %}

The plugin includes a large range of features such as:

- Complete highlighting of HyperList elements
- Collapsing and expanding of up to 15 levels in a list
- Linking/referencing between elements (items) in a list
- Easy navigation in lists, including jumping to references
- "Presentation mode" where you can view only parts of lists and line-by-line
- Highlight only the current part of a HyperList
- Automatic underlining of State or Transition items in a list
- Creating and checking of checkboxes in a list, with or without date stamps
- Easy navigation to elements that needs filling out (when you use a list as a template)
- Encryption (and decryption) of whole lists or parts of lists
- Auto-encryption of lists - making a list into an excellent password safe
- HTML, LaTeX and TPP export of HyperLists
- Show or hide all lines with word under cursor
- Add all items tagged with future dates to your Google calendar
- Description on how to include HyperLists within other filetypes, thus taking full advantage of the above features when including a HyperList in e.g. a normal .txt document or an e-mail.
- All documents with the file suffix ".hl" is treated as HyperList documents
- ... and there are many more features. Check out the comprehensive documentation (type ":help HyperList" in VIM after install)

Go to the <a href="http://www.vim.org/scripts/script.php?script_id=4006">HyperList VIM plugin page</a> (<a href="https://github.com/isene/hyperlist.vim" target="_blank" rel="noopener">source on Github</a>).

##### Writing HyperLists in VIM on Android
To work with HyperLists in VIM on your Android phone, you can follow a few, simple steps:
1. Download [Termux for Android](https://play.google.com/store/apps/details?id=com.termux)
2. Start Termux and type: pkg install vim
3. Download the HyperList VIM plugin ([hyperlist.vmb](https://www.vim.org/scripts/script.php?script_id=4006)) on your Android
4. In Termux write: <b>cp /storage/emulated/0/Download/hyperlist.vmb .</b>
5. In termux write: <b>vim hyperlist.vmb</b>
6. This gets you into VIM, then write: <b>:so %</b> (and press Enter) This installs HyperList in your VIM
7. To quit VIM write: <b>:q</b>
8. To use encryption within HyperLists, do: pkg install openssl openssl-tool

#### HyperList mode for EMACS
[Vifon](https://github.com/Vifon) (that I know from the
[Ranger](https://ranger.github.io/) IRC channel) have created a [HyperList
mode for EMACS](https://github.com/vifon/hyperlist-mode).

#### HyperGraph
You can automatically graph a HyperList as either a mindmap (for HyperLists that are State descriptions) or a flowchart (for HyperLists that are Transitions descriptions). An example should suffice - this dummy HyperList:
<pre><strong>First Item</strong>
   Second Item<span style="color:green;">;</span> <span style="color:blue;">OR: </span>
      Third Item
      Fourth Item
   Fifth Item
   <span style="color:green;">[? Item=Cool]</span> Sixth Item <span style="color:teal;">(</span><span style="color:magenta;">〈Second Item〉</span><span style="color:teal;">)</span>
   Seventh Item
   Eighth Item
</pre>
<br />
Graphed as a State (mindmap):

![](/assets/img/test_state1.png)

Graphed as a Transition (flowchart):

<img src="/assets/img/test_trans1.png" width="200" />

You may [graph your HyperLists with the online HyperGraph](https://isene.com/hypergraph.html)

HyperGraph is a [Ruby](http://en.wikipedia.org/wiki/Ruby_(programming_language)) script with a lot of options. Download [HyperGraph here](https://github.com/isene/hypergraph). HyperGraph is a rather complex endeavour. It works but you may encounter some snags. If you do, drop me a line and I will fix.
