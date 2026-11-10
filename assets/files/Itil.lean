/-
  Play: write "ITIL a Simpler Way" as exact rules, and let Lean check what is true in
  every state the process can reach.
  Source: the guide "ITIL pragmatic and simple" (Incident, Problem and Change Management,
  Release & Deployment).
  Check it with:  lean Itil.lean
  No output means every proof below is accepted. Core Lean 4 only.

  The model: any number of Incidents, Problems, RfCs and Releases. A state says where
  every ticket is. A step is one move the process text allows.
  Left out: Service Desk routing, Request Fulfillment, the three test platforms, PIR.

  What Lean shows.
  Rules that are true in every reachable state:
  * A Release only ships an approved RfC (`release_needs_approval`).
  * A closed Incident is mitigated or has a Problem ticket that exists
    (`closed_incident_is_covered`).
  * A closed Problem was solved by a Standard Change or has an approved RfC
    (`closed_problem_has_a_change`).
  Gaps in the text as written:
  * The Change Policy names no decider for Impact 3 (`impact_three_has_no_decider`).
  * An Incident can close while the user is still down. "No solution found" jumps to
    "Create Problem Ticket", past "Verify with originator" (`incident_closes_unmitigated`).
  * A Problem can close before its Change is released. Its process goes on when the RfC
    is approved, and never waits for the Release (`problem_closes_before_release`).
  * A Problem whose RfCs are all rejected never closes (`closed_problem_has_a_change`).
  The four fixes, and the proof that each gap is gone:
  * Change Policy, third line: "Impact ≥ 3" (`every_impact_has_a_decider`).
  * An Incident closes only when the originator confirms it is mitigated. A Problem
    ticket alone is not enough (`closed_incident_is_mitigated`).
  * Problem Management waits for the Release before "Verify with the ticket creator"
    (`closed_problem_is_released`).
  * A Problem may end as "won't fix" when its RfC is rejected, and only then
    (`rejected_problem_can_end`, `wont_fix_needs_a_rejection`).
-/

/-! ## The Change Policy
  "[? Impact < 3 AND Competence > 3] Individual resource can decide on the Change
   [? Impact < 3] Change Manager decides on the Change
   [? Impact > 3] Change Manager decides on the Change after CAB" -/

/-- Some line of the Change Policy says who decides. -/
def hasDecider (impact competence : Nat) : Prop :=
  (impact < 3 ∧ competence > 3) ∨ impact < 3 ∨ impact > 3

/-- Gap: no line covers Impact 3. -/
theorem impact_three_has_no_decider (competence : Nat) : ¬ hasDecider 3 competence := by
  simp [hasDecider]

/-- Every other Impact has a decider. -/
theorem other_impacts_have_a_decider (impact competence : Nat) (h : impact ≠ 3) :
    hasDecider impact competence := by
  simp only [hasDecider]; omega

/-- The fix: the third line reads "Impact ≥ 3". -/
def hasDeciderFixed (impact competence : Nat) : Prop :=
  (impact < 3 ∧ competence > 3) ∨ impact < 3 ∨ impact ≥ 3

theorem every_impact_has_a_decider (impact competence : Nat) :
    hasDeciderFixed impact competence := by
  simp only [hasDeciderFixed]; omega

/-! ## The tickets and the moves -/

inductive Inc | none | opened | closed
inductive Prob | none | analysing | waiting | verifying | closed | wontFix
inductive Chg | none | submitted | rejected | approved

/-- Where every ticket is. Tickets are numbered; `none` means "not made yet". -/
structure State where
  inc : Nat → Inc
  /-- The originator has confirmed that the Incident is mitigated. -/
  mitigated : Nat → Bool
  /-- The Problem ticket made from an Incident, if any. -/
  incProb : Nat → Option Nat
  prob : Nat → Prob
  /-- The Problem's solution was done as a Standard Change. -/
  viaStc : Nat → Bool
  /-- The RfC a Problem last submitted, if any. -/
  probChg : Nat → Option Nat
  /-- An RfC. `approved` also means its Work Package exists. -/
  chg : Nat → Chg
  /-- The RfC a Release ships, if the Release is made. -/
  rel : Nat → Option Nat

/-- The start: no tickets. -/
def init : State :=
  ⟨fun _ => .none, fun _ => false, fun _ => none, fun _ => .none, fun _ => false,
   fun _ => none, fun _ => .none, fun _ => none⟩

/-- `f`, with ticket `i` moved to `v`. -/
def put {α : Type} (f : Nat → α) (i : Nat) (v : α) : Nat → α :=
  fun j => if j = i then v else f j

/-- The moves the process allows. Incident Management, then Problem Management,
    Change Management, and Release & Deployment.
    `fixed = false` is the text as written. `fixed = true` adds three fixes: an
    Incident closes only when mitigated, a Problem goes on only when its Change is
    released, and a Problem may end as "won't fix" when its RfC is rejected. -/
inductive Step (fixed : Bool) : State → State → Prop
  | receive (s : State) (i : Nat) : s.inc i = .none →
      Step fixed s { s with inc := put s.inc i .opened }
  | mitigate (s : State) (i : Nat) : s.inc i = .opened →
      Step fixed s { s with mitigated := put s.mitigated i true }
  | createProblem (s : State) (i p : Nat) :
      s.inc i = .opened → s.incProb i = none → s.prob p = .none →
      Step fixed s { s with incProb := put s.incProb i (some p), prob := put s.prob p .analysing }
  | closeInc (s : State) (i : Nat) :
      s.inc i = .opened →
      (s.mitigated i = true ∨ (fixed = false ∧ s.incProb i ≠ none)) →
      Step fixed s { s with inc := put s.inc i .closed }
  | proactive (s : State) (p : Nat) : s.prob p = .none →
      Step fixed s { s with prob := put s.prob p .analysing }
  | submitRfc (s : State) (p c : Nat) : s.prob p = .analysing → s.chg c = .none →
      Step fixed s { s with prob := put s.prob p .waiting, probChg := put s.probChg p (some c),
                            chg := put s.chg c .submitted }
  | standardChange (s : State) (p : Nat) : s.prob p = .analysing →
      Step fixed s { s with prob := put s.prob p .verifying, viaStc := put s.viaStc p true }
  | rfcRejected (s : State) (p c : Nat) :
      s.prob p = .waiting → s.probChg p = some c → s.chg c = .rejected →
      Step fixed s { s with prob := put s.prob p .analysing }
  | rfcApproved (s : State) (p c : Nat) :
      s.prob p = .waiting → s.probChg p = some c → s.chg c = .approved →
      (fixed = true → ∃ r, s.rel r = some c) →
      Step fixed s { s with prob := put s.prob p .verifying }
  | wontFix (s : State) (p c : Nat) : fixed = true →
      s.prob p = .waiting → s.probChg p = some c → s.chg c = .rejected →
      Step fixed s { s with prob := put s.prob p .wontFix }
  | notSolved (s : State) (p : Nat) : s.prob p = .verifying →
      Step fixed s { s with prob := put s.prob p .analysing }
  | closeProb (s : State) (p : Nat) : s.prob p = .verifying →
      Step fixed s { s with prob := put s.prob p .closed }
  | otherRfc (s : State) (c : Nat) : s.chg c = .none →
      Step fixed s { s with chg := put s.chg c .submitted }
  | approve (s : State) (c : Nat) : s.chg c = .submitted →
      Step fixed s { s with chg := put s.chg c .approved }
  | reject (s : State) (c : Nat) : s.chg c = .submitted →
      Step fixed s { s with chg := put s.chg c .rejected }
  | release (s : State) (r c : Nat) : s.rel r = none → s.chg c = .approved →
      Step fixed s { s with rel := put s.rel r (some c) }

/-- `t` can be reached from `s` in some number of moves. -/
inductive Reach (fixed : Bool) (s : State) : State → Prop
  | refl : Reach fixed s s
  | step {t u : State} : Reach fixed s t → Step fixed t u → Reach fixed s u

/-- What stays true after every move. -/
structure Safe (s : State) : Prop where
  incOk : ∀ i, s.inc i = .closed → s.mitigated i = true ∨ s.incProb i ≠ none
  linked : ∀ i p, s.incProb i = some p → s.prob p ≠ .none
  probOk : ∀ p, s.prob p = .verifying ∨ s.prob p = .closed →
    s.viaStc p = true ∨ ∃ c, s.probChg p = some c ∧ s.chg c = .approved
  relOk : ∀ r c, s.rel r = some c → s.chg c = .approved

theorem safe_step {fixed : Bool} {s t : State} (h : Safe s) (st : Step fixed s t) : Safe t := by
  obtain ⟨h1, h2, h3, h4⟩ := h
  cases st <;> refine ⟨?_, ?_, ?_, ?_⟩ <;> simp only [put] <;> intro a <;>
    (try (intro b; revert b)) <;> (repeat' split) <;> intros <;>
    first
      | exact h1 _ (by assumption)
      | exact h2 _ _ (by assumption)
      | exact h3 _ (by assumption)
      | exact h4 _ _ (by assumption)
      | (simp_all; done)
      | (have := h2 _ _ (by assumption); split <;> simp_all; done)
      | (have := h4 _ _ (by assumption); split <;> simp_all; done)
      | (grind; done)
      | (rcases h3 _ (by assumption) with hv | ⟨c, hc1, hc2⟩
         · exact Or.inl hv
         · refine Or.inr ⟨c, hc1, ?_⟩; split <;> simp_all)

theorem safe_init : Safe init where
  incOk := by intro _ h; cases h
  linked := by intro _ _ h; cases h
  probOk := by intro _ h; cases h <;> rename_i h <;> cases h
  relOk := by intro _ _ h; cases h

theorem safe_reach {fixed : Bool} {s : State} (h : Reach fixed init s) : Safe s := by
  induction h with
  | refl => exact safe_init
  | step _ st ih => exact safe_step ih st

/-! ## Rules that are true in every reachable state, with or without the fixes -/

/-- A Release only ships an approved RfC. -/
theorem release_needs_approval {fixed : Bool} {s : State} (h : Reach fixed init s) (r c : Nat)
    (hr : s.rel r = some c) : s.chg c = .approved :=
  (safe_reach h).relOk r c hr

/-- A closed Incident is mitigated, or has a Problem ticket that exists. -/
theorem closed_incident_is_covered {fixed : Bool} {s : State} (h : Reach fixed init s) (i : Nat)
    (hi : s.inc i = .closed) :
    s.mitigated i = true ∨ ∃ p, s.incProb i = some p ∧ s.prob p ≠ .none := by
  cases (safe_reach h).incOk i hi with
  | inl hm => exact Or.inl hm
  | inr hp =>
    cases hl : s.incProb i with
    | none => exact (hp hl).elim
    | some p => exact Or.inr ⟨p, rfl, (safe_reach h).linked i p hl⟩

/-- A closed Problem was solved by a Standard Change, or has an approved RfC. -/
theorem closed_problem_has_a_change {fixed : Bool} {s : State} (h : Reach fixed init s) (p : Nat)
    (hp : s.prob p = .closed) :
    s.viaStc p = true ∨ ∃ c, s.probChg p = some c ∧ s.chg c = .approved :=
  (safe_reach h).probOk p (Or.inr hp)

/-! ## Gaps: states the text as written allows -/

/-- An Incident closes while the user is still down. The path: receive Incident 0,
    find no solution and create Problem 0, close the Incident. -/
theorem incident_closes_unmitigated :
    ∃ s, Reach false init s ∧ s.inc 0 = .closed ∧ s.mitigated 0 = false := by
  refine ⟨_, .step (.step (.step .refl (.receive init 0 rfl))
    (.createProblem _ 0 0 rfl rfl rfl)) (.closeInc _ 0 rfl (Or.inr ⟨rfl, ?_⟩)), rfl, rfl⟩
  simp [put]

/-- A Problem closes before its Change is released. The path: make Problem 0, submit
    RfC 0, approve it, go on to "verify", close. No Release was made. -/
theorem problem_closes_before_release :
    ∃ s, Reach false init s ∧ s.prob 0 = .closed ∧ s.probChg 0 = some 0 ∧ ∀ r, s.rel r ≠ some 0 := by
  refine ⟨_, .step (.step (.step (.step (.step .refl (.proactive init 0 rfl))
    (.submitRfc _ 0 0 rfl rfl)) (.approve _ 0 rfl)) (.rfcApproved _ 0 0 rfl rfl rfl (fun h => by cases h)))
    (.closeProb _ 0 rfl), rfl, rfl, ?_⟩
  intro r h; cases h

/-! ## The fixes close the two gaps -/

/-- What stays true after every move of the fixed process. -/
structure Strict (s : State) : Prop where
  incOk : ∀ i, s.inc i = .closed → s.mitigated i = true
  probOk : ∀ p, s.prob p = .verifying ∨ s.prob p = .closed →
    s.viaStc p = true ∨ ∃ c r, s.probChg p = some c ∧ s.rel r = some c
  wontFixOk : ∀ p, s.prob p = .wontFix → ∃ c, s.probChg p = some c ∧ s.chg c = .rejected

theorem strict_step {s t : State} (h : Strict s) (st : Step true s t) : Strict t := by
  obtain ⟨h1, h2, h3⟩ := h
  cases st <;> refine ⟨?_, ?_, ?_⟩ <;> simp only [put] <;> intro a <;>
    (repeat' split) <;> intros <;>
    first
      | exact h1 _ (by assumption)
      | exact h2 _ (by assumption)
      | (simp_all; done)
      | (rcases h2 _ (by assumption) with hv | ⟨c, r, hc, hr⟩
         · exact Or.inl hv
         · refine Or.inr ⟨c, r, hc, ?_⟩; split <;> simp_all)
      | (obtain ⟨c, hc1, hc2⟩ := h3 _ (by assumption)
         refine ⟨c, hc1, ?_⟩; split <;> simp_all)
      | exact h3 _ (by assumption)

theorem strict_init : Strict init where
  incOk := by intro _ h; cases h
  probOk := by intro _ h; cases h <;> rename_i h <;> cases h
  wontFixOk := by intro _ h; cases h

theorem strict_reach {s : State} (h : Reach true init s) : Strict s := by
  induction h with
  | refl => exact strict_init
  | step _ st ih => exact strict_step ih st

/-- Fixed: a closed Incident is mitigated. -/
theorem closed_incident_is_mitigated {s : State} (h : Reach true init s) (i : Nat)
    (hi : s.inc i = .closed) : s.mitigated i = true :=
  (strict_reach h).incOk i hi

/-- Fixed: a closed Problem was solved by a Standard Change, or its Change is released. -/
theorem closed_problem_is_released {s : State} (h : Reach true init s) (p : Nat)
    (hp : s.prob p = .closed) :
    s.viaStc p = true ∨ ∃ c r, s.probChg p = some c ∧ s.rel r = some c :=
  (strict_reach h).probOk p (Or.inr hp)

/-- Fixed: a Problem ends as "won't fix" only when its RfC was rejected. -/
theorem wont_fix_needs_a_rejection {s : State} (h : Reach true init s) (p : Nat)
    (hp : s.prob p = .wontFix) : ∃ c, s.probChg p = some c ∧ s.chg c = .rejected :=
  (strict_reach h).wontFixOk p hp

/-- Fixed: a Problem whose RfC is rejected has a way out. -/
theorem rejected_problem_can_end (s : State) (p c : Nat) (hp : s.prob p = .waiting)
    (hc : s.probChg p = some c) (hr : s.chg c = .rejected) :
    ∃ t, Step true s t ∧ t.prob p = .wontFix :=
  ⟨_, .wontFix s p c rfl hp hc hr, by simp [put]⟩
