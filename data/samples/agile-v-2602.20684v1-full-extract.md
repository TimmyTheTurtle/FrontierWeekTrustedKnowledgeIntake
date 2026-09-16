# Extracted page 1

Agile V: A Compliance-Oriented Framework for
AI-Augmented Engineering — From Concept to
Audit-Ready Delivery
Christopher Koch
Agile-V .org
Germany
https://agile-v.org
Joshua A. Wellbrock
Agile-V .org
Germany
https://agile-v.org
Abstract—Current AI-assisted engineering workflows lack a
built-in mechanism to maintain task-level verification and regu-
latory traceability at machine-speed delivery. Agile V addresses
this gap by embedding independent verification and audit artifact
generation into each task cycle. The framework merges Agile
iteration with V-Model verification into a continuousInfinity
Loop, deploying specialized AI agents for requirements, design,
build, test, and compliance—governed by mandatory human
approval gates. We evaluate three hypotheses: (H1) audit-oriented
artifacts emerge as a by-product of development, (H2) 100%
requirement-level verification is achievable with independent test
generation, and (H3) verified increments can be delivered with
single-digit human interactions per cycle. A feasibility case study
on a Hardware-in-the-Loop system (≈500 LOC, 8 requirements,
54 tests) supports all three hypotheses: audit-oriented documen-
tation was generated automatically (H1), 100% requirement-level
pass rate was achieved (H2), and only 6 prompts per cycle
were required (H3)—yielding an estimated 10–50×cost reduction
versus a COCOMO II baseline (sensitivity range from pessimistic
to optimistic assumptions). These results demonstrate feasibility
on a bounded, well-defined project; generalizability to larger
or more ambiguous systems remains to be established through
independent replication.
Index Terms—Agile, V-Model, AI-augmented engineering, veri-
fication, traceability, quality management, regulatory compliance,
open standard, GMP, GxP, ISO 9001, ISO 13485, GAMP 5,
21 CFR Part 11
I. INTRODUCTION
AI coding assistants have moved from pilot programs
toward broad organizational adoption [1], [2]. Engineering
teams now routinely generate code, tests, and documentation
at a pace that was unthinkable two years ago [3]. Yet this
acceleration exposes a structural weakness:current AI-assisted
engineering workflows are missing a built-in mechanism to
maintain task-level verification and regulatory traceability at
machine-speed delivery[4]–[6].
The resulting business risk is evident. Organizations in
regulated industries face audit findings when development
artifacts lack traceability [5]–[8]. Product teams can ship
faster, but deferring compliance work can accumulate com-
pliance debt that surfaces during certification or customer
audits [5]–[7]. Quality managers struggle to enforce review
disciplines when the volume of generated work overwhelms
human reviewers [9].
The two dominant paradigms each solve only half the
problem:
•Scrum[10] optimizes for adaptability and speed but
provides no built-in mechanism for verification, traceabil-
ity, or regulatory documentation [5]—a gap that widens
further at the pace AI agents produce.
•V-Model[11] delivers the rigor and traceability regu-
lators expect but is project-bound, phase-gated, and too
slow for continuous AI-driven delivery.
Agile V1 addresses this gap by embedding independent veri-
fication and audit artifact generation into each task cycle. It is a
unified open standard (CC BY-SA 4.0 [12]) that merges Agile
iteration with V-Model verification into a single, repeatable
workflow—theInfinity Loop—executed continuously at the
task level. The framework is operationalized through a library
of composable AI agent skills [13] that any organization can
deploy within existing toolchains.
This paper presents both a conceptual framework and a
feasibility case study. We evaluate Agile V against three
hypotheses:
•H1 (Audit-Evidence By-Product):Using Agile V’s In-
finity Loop with human approval gates, a small AI-agent
team can produce a structured audit-evidence artifact
set (requirements specification, traceability matrix, test
evidence, decision log) as a by-product of development
for a bounded project.
•H2 (Verification Pass Rate):For a bounded system,
Agile V can achieve 100% requirement-level verification
pass rate with independent test generation.
•H3 (Minimal Human Interaction):For a bounded
system, Agile V can deliver a working, verified increment
with a small number of human interactions per cycle (e.g.,
single-digit prompts) while maintaining full traceability.
We evaluate these hypotheses through a Hardware-in-the-
Loop (HIL) case study spanning two Infinity Loop cycles.
1Agile V is a trademark of Agile-V .org.
arXiv:2602.20684v1  [cs.SE]  24 Feb 2026

# Extracted page 2

The study quantifies the business impact: an estimated 10–50×
cost reduction (versus a COCOMO II baseline, depending on
assumptions; see Section V-D) with structured audit-evidence
documentation produced as a by-product of the engineering
workflow. The second cycle validates the framework’s iterative
correction mechanism, showing that AI-generated artifacts can
be systematically hardened through structured change requests.
II. RELATEDWORK
A. Agile and V-Model Hybrids
Several attempts have been made to reconcile Agile iteration
with V-Model verification. The W-Model [14] extends the
V-Model by introducing early test activities in parallel with
each development phase, reducing the delay between design
and verification. Yet, the W-Model remains project-scoped
and does not address continuous, task-level verification. The
Scaled Agile Framework (SAFe) [15] adds governance layers
to Scrum, including compliance and regulatory tracks, but does
not prescribe how AI-generated artifacts should be verified
or how traceability should be maintained at machine speed.
Agile V differs from both by operating at theindividual task
level and by embedding verification as a structural constraint
of the workflow rather than as an optional overlay.
B. DevSecOps and Automated Compliance
DevSecOps pipelines [16] integrate security and compliance
checks into CI/CD workflows, typically through static analysis,
container scanning, and policy-as-code gates. While these
pipelines automateexecutionof predefined checks, they do
not generate the compliance artifacts themselves (e.g., require-
ments specifications, traceability matrices, decision rationale
logs). Agile V complements DevSecOps by producing these
artifacts as a workflow by-product, enabling organizations
to adopt both approaches: DevSecOps for infrastructure-level
controls and Agile V for engineering-level verification and
documentation.
C. AI-Assisted Software Engineering
Recent empirical studies have measured the productivity
impact of AI coding assistants. Peng et al. [3] reported a
55.8% task completion speedup with GitHub Copilot, while
Dell’Acqua et al. [1] found that AI-assisted consultants pro-
duced 40% higher quality work—but only within the model’s
capability boundary. He et al. [4] demonstrated that unstruc-
tured AI-assisted development increases code complexity and
technical debt over time. These findings collectively motivate
Agile V’s design: the framework captures the productivity
gains documented by Peng et al. and Dell’Acqua et al. while
mitigating the quality risks identified by He et al. through
mandatory verification gates and independent test generation.
D. LLM-Based Test Generation
Recent work uses LLMs to generate tests fromcode:
CodaMosa [17] combines search-based generation with LLM-
produced seeds to improve branch coverage, and ChatU-
niTest [18] achieves competitive coverage when guided by
focal-method context. These tools maximizecode-levelcov-
erage. Agile V’s Test Designer differs by generating tests
fromrequirements only, ensuring structural independence be-
tween build and verification. The approaches are complemen-
tary: LLM-based coverage tools could augment Agile V’s
requirement-level suite in future work.
E. Spec-Driven AI Development Tools
A growing class of open-source tools addresses context
management and task orchestration for AI coding agents.
Representative examples include Get Shit Done (GSD) [19],
BMAD, and SpecKit—meta-prompting systems that decom-
pose projects into phases, spawn parallel sub-agents, and
manage context window limits. These tools areproductivity
tooling, notprocess frameworks: they optimize how an AI
agent builds code but prescribe neither independent verifica-
tion (build and test share context), nor regulatory traceability
(no requirement-to-test mapping or audit trail), nor human
governance gates.
Agile V operates at a different abstraction level: where GSD
is abuild accelerator, Agile V is anengineering processthat
ensures artifacts are verifiable, traceable, and structured for
audit review. In v1.3 [13], we integrated GSD’s execution-
layer patterns into the skills library with one constraint: all
GSD-derived mechanisms operatewithinthe Infinity Loop’s
verification boundaries, demonstrating that productivity tool-
ing and process governance can be composed.
III. THEAGILEV FRAMEWORK
A. Core Principles
Agile V is built on four operational principles that redefine
how engineering organizations use AI while maintaining the
governance that regulators, auditors, and customers demand:
1)Verified Iterationover Unchecked Velocity — Every
AI-generated artifact is tested before it advances. Speed
is a by-product of confidence, not a substitute for it.
2)Traceable Agencyover Opaque Autonomy — The audit
trail recordswho—human or AI agent—made each deci-
sion andwhy, satisfying the accountability requirements
of ISO 9001 [20] and GxP regulations.
3)Living Complianceover Static Documentation — Reg-
ulatory documentation is generated as a by-product
of the engineering workflow, eliminating the post-hoc
“documentation sprint” that delays releases.
4)Human Curationover Human Execution — Engineers
shift from writing code to directing intent, reviewing de-
signs, and approving releases. AI handles the execution;
humans retain authority.
B. The Infinity Loop Workflow
The central mechanism of Agile V is theInfinity Loop
(Fig. 1), a continuous workflow that replaces sequential project
phases with a repeatable cycle executed on every task:

# Extracted page 3

Intent
Decomp.
Gate 1
Build Test
Red Team
Audit
Gate 2
Definition
Validation
Fig. 1. The Agile V Infinity Loop: Definition (top) flows through Synthesis
(center) to Validation (bottom), with a feedback path closing the loop.
1) Definition — Intent & Decomposition:An engineer
provides high-levelProduct Intent(e.g., “build a HIL test
system for this analyzer”). TheRequirement Architectagent
decomposes it into atomic, traceable requirements with explicit
acceptance criteria. TheLogic Gatekeepervalidates feasibil-
ity against physical and organizational constraints.Human
Gate 1ensures the team agrees on scope before any code
is written.
2) Apex — Synthesis:Two agents workin parallelto pre-
vent confirmation bias—a key differentiator from traditional
code-then-test workflows:
•TheBuild Agentgenerates deliverables (code, schemat-
ics, configuration).
•TheTest Designercreates a verification suite from
therequirements only—never from the code—ensuring
independent test coverage.
3) Validation — Verification & Compliance:TheRed
Team Verifierexecutes the test suite against the build artifacts
and produces an objective pass/fail report. TheCompliance
Auditorcaptures the full decision rationale—whyeach design
choice was made—generating structured audit-evidence logs
in real time.Human Gate 2gives the responsible engineer
final approval authority before release.
C. Context Engineering
A practical challenge for any AI-agent-based workflow
iscontext window degradation: as a session accumulates
tokens, model reasoning quality declines [19]. Agile V v1.3
addresses this by aligning context boundaries with V-Model
positions. Definition-phase agents read requirement files di-
rectly; Synthesis agents (Build Agent, Test Designer) receive
requirement IDs and paths but operate in separate, fresh
contexts; Validation-phase agents (Red Team Verifier) never
inherit Build Agent context, preserving the independence
required by the Red Team Protocol. A thin orchestrator (≈10–
15% of the context window) coordinates agents, passing file
references rather than file contents, and spawning fresh sub-
agent contexts so that no single session exceeds 50% of the
available window. Independent tasks are parallelized inwaves
with fresh context per agent—enabling the Build Agent and
Test Designer to synthesize concurrently without shared state.
D. Persistent Memory
Agent sessions start without implicit repository knowledge,
so exploration-only workflows tend to re-discover constraints
and miss non-obvious conventions. Agile V therefore main-
tainspersistent memoryas a curated, version-controlled store
of high-signal project knowledge (entrypoints, commands,
invariants, and decision rationales) that tells agentswhere to
lookand what must not change.
To keep active context small, long-lived knowledge is
retrieved on demand rather than re-injected wholesale [21],
using bounded working-memory strategies to fit within a
session [22]. Persistent memory should store non-sensitive
summaries and file pointers rather than secrets or proprietary
raw logs.
IV. CASESTUDY: HIL TESTSYSTEM
To demonstrate Agile V on a representative industrial
project, the framework was applied to deliver a Python-based
Hardware-in-the-Loop (HIL) test environment for a Saleae
Logic Analyzer—the type of system commonly required in
electronics manufacturing, automotive validation, and medical
device verification.
A. Project Scope
The deliverable (Fig. 2) had to meet four operational re-
quirements typical of production test systems:
•Abstraction of device communication (DUT) for multi-
product reuse.
•Automation of the Saleae Logic 2 software via its
API [23].
•Synchronization of test scripts with hardware capture (<
100ms latency).
•Jupyter Notebook integration for engineering analysis and
reporting.

# Extracted page 4

Pytest Suite
Logic API
Device Mgr
Logic Pro 16
DUT
Host PC
Hardware
USB
Probes
(Mock Mode)
Fig. 2. System Architecture: Agile V Agents generated the Python Host
components (top), integrating with the physical Logic Analyzer (bottom).
B. Study Design
The case study follows a single-case embedded design [5]
with two units of analysis (Cycle 1: initial delivery; Cycle 2:
change request). The study was conducted by the framework’s
authors, which introduces potential bias (Section VI-E).
Evaluation criteria.Each hypothesis maps to observable
metrics: H1 is evaluated by the presence and completeness
of six artifact types (requirements spec, traceability matrix,
test log, decision rationale, risk register, validation summary);
H2 by the requirement-level pass rate and the number of Red
Team findings; H3 by the count of human prompts per cycle.
Data collection.All agent interactions were conducted
through commercial AI platforms (Gemini 1.5 Pro for Cycle 1,
Claude Opus 4.6 for Cycle 2). Prompt counts, artifact invento-
ries, and test results were recorded from the session logs and
the.agile-v/state directory. The COCOMO II baseline was
estimated independently of the case study execution.
C. Delivery Execution
The project completed two full passes through the Infinity
Loop, demonstrating both initial delivery (Cycle 1) and itera-
tive hardening (Cycle 2).
1) Cycle 1 — Initial Delivery:
1)Intent:The project lead described the HIL system and
its hardware constraints in plain language.
2)Decomposition:The Requirement Architect produced
7 formal requirements (REQ-0001 to REQ-0007) with
measurable acceptance criteria, including “Mock De-
vice” mode for CI/CD environments without physical
hardware.
3)Gate 1:The Logic Gatekeeper verified that
Python 3.10+ and thesaleae-automationSDK
were available and compatible. The project lead
approved the Blueprint.
4)Synthesis:The Build Agent deliveredsrc/hil/(Logi-
cAnalyzer wrapper, DeviceManager) while the Test De-
signer independently createdtests/andnotebooks/.
5)Verification:The Red Team Verifier executed the initial
test suite, achieving a 100% pass rate at the requirement
level. However, the Cycle 1 suite was narrower than
the final 54-test suite: it covered the functional contract
of each module but lacked the input validation, cycle-
field, and state-directory tests that Cycle 2 later added.
The first-pass success should therefore be read with the
caveat that the test surface was expanded significantly
in the subsequent cycle.
2) Cycle 2 — Change Request and Compliance Hardening:
Cycle 2 was triggered by CR-0001 (Agile V Skill Upgrade
v1.3), which required structural changes across the codebase:
1)Intent:Upgrade to vendor-agnostic device abstraction,
add multi-cycle traceability, and harden compliance ar-
tifacts.
2)Decomposition:The Requirement Architect added
REQ-0008 (.agile-v/state directory for persistent
process state) and modified 4 existing requirements to
incorporate cycle-aware fields. The total grew from 7 to
8 verified requirements.
3)Gate 1:The Logic Gatekeeper validated the change
scope.
4)Synthesis:The Build Agent refactored
DeviceInterfacefrom a vendor-specific SDK
binding to a transport-agnostic Abstract Base Class,
added acyclefield toTestResultand the logging
subsystem, and introduced a GitHub Actions CI pipeline
testing Python 3.10–3.13. The Test Designer expanded
the suite from the initial set to54 automated tests.
5)Verification:The Red Team Verifier identified10 find-
ings(6 MAJOR, 4 MINOR)—including stale API ref-
erences, a missingcyclefield, an async property anti-
pattern, and input validation gaps. All MAJOR findings
were resolved by the Build Agent; the test suite achieved
54/54 pass post-rework.

# Extracted page 5

This second cycle is significant because it demonstrates the
Infinity Loop operating as designed: a change request triggered
a controlled iteration, Red Team findings drove concrete fixes,
and full traceability was maintained across cycles—exactly the
corrective-action loop that ISO 9001:2015 Clause 10.2 [20]
requires.
D. Operational Metrics
The complete system—source code, tests, documentation,
and configuration—was delivered across two cycles with min-
imal engineer involvement:
TABLE I
SESSIONMETRICS(AFTERCYCLE2)
Metric Scope Value
Verified Requirements Cumulative 8
Automated Tests Cumulative 54
Source Code Cumulative≈500 LOC
User Prompts Per cycle 6
Red Team Findings C2 only 10 (all resolved)
CI Matrix Cumulative 4 Python versions
The metrics in Table I serve as the primary data source for
evaluating H1–H3 in Section VI.
E. Tooling and Infrastructure
Agile V requires only commercially available AI plat-
forms. The case study used Gemini 1.5 Pro (Cycle 1) and
Claude Opus 4.6 (Cycle 2), demonstrating model-agnosticism
empirically—the text-based agent skills are independent of
the underlying model, and.agile-v/config.jsontracks
which provider was used per cycle for auditability. The context
engineering mechanisms (Section III-C) decompose work into
sub-agent scopes of≤50% window utilization, making the
framework viable on models with smaller context windows
than those used in the case study.
Cycle 2 introduced a.agile-v/state directory (REQ-
0008) that persists process artifacts (configuration, change log,
approvals, risk register, traceability matrix, Red Team report,
validation summary) alongside source code in version control,
serving as both agent context for cross-session continuity and
as an evidence bundle for audit review.
V. BUSINESSCASE
To quantify the return on investment, the recorded Agile V
session was compared against industry-standard benchmarks
for a traditional team delivering the same scope: a HIL test
system with ISO 9001:2015 [20] documentation.
A. Baseline: Traditional Delivery
The traditional estimate is derived from COCOMO II para-
metric cost modeling [24], calibrated for a quality-critical
embedded test system of moderate complexity:
•Requirements & Architecture:16 hours (2 days).
•Implementation:40 hours (1 week).
•Test Engineering:24 hours (3 days).
•Compliance Documentation:24 hours (3 days).
•Total Effort:≈104 hours (2.5 weeks).
•Estimated Cost:$15,600 (at $150/hr blended rate).
This estimate is conservative. The Standish Group’s CHAOS
data [25] reports that only 29% of IT projects are delivered on
time and on budget; the remainder experience cost overruns
averaging 45% or fail outright—suggesting the true expected
cost is likely higher.
B. Agile V Delivery Cost Across Models
The Agile V framework is model-agnostic. To illustrate the
cost range, Table II compares the compute cost of the HIL
case study (estimated at≈500k input tokens,≈25k output
tokens based on session length and average file sizes) across
representative commercially available models. Gemini 1.5 Pro
values report the observed Cycle 1 billed compute total; all
other rows use February 2026 API list pricing estimates [26]–
[28].
TABLE II
AI COMPUTECOST BYMODEL(HIL CASESTUDY)
Model Input Output Total
Gemini 1.5 Pro * $1.75 $2.63 $4.38
Gemini 2.5 Pro $0.63 $0.25 $0.88
Claude Sonnet 4.6 $1.50 $0.38 $1.88
Claude Opus 4.6 $2.50 $0.63 $3.13
GPT-5 mini $0.13 $0.05 $0.18
GPT-5.2 $0.88 $0.35 $1.23
*Gemini 1.5 Pro values are the Cycle 1 billed
compute total. All other rows are list-price estimates
using the same token counts; Gemini 2.5 Pro
assumes the standard (<=200k prompt) pricing
tier [27]. Pricing varies by provider features (e.g.,
caching, batching, long-context tiers).
Including 4 hours of engineer time at $150/hr, theper-cycle
project cost ranges from$601to$605across the models in
Table II. The AI compute cost is negligible relative to human
effort in all cases—representing less than 1% of the total.
Methodological notes:
1) The Agile V cost figure captures the direct execution
cost (human gate-review time plus AI compute) for a
single cycle. The case study completed two cycles; the
total observed cost is approximately $1,200 (2×4 hours
+≈$10 compute). The baseline 25×figure is based on
a single delivery cycle; the sensitivity range is 10–50×
(Section V-D).
2) The traditional baseline ($15,600) is a COCOMO IIesti-
mate, not a measured cost. The comparison is therefore
between a parametric model and an observed session,
which limits the precision of the ratio.
3) One-time adoption costs (framework learning, skill con-
figuration) are excluded and estimated at 8–16 hours
for a team’s first Agile V deployment. These costs are
amortized across projects.

# Extracted page 6

C. Impact Summary
•Cost:Estimated 10–50×reduction ($15,600 CO-
COMO II baseline→$601–$605 observed per cycle;
96% at baseline).
•Time-to-delivery:Estimated 25×acceleration
(2.5 weeks baseline→4 hours observed per cycle).
•Compliance coverage:Higher artifact completeness than
typical for a 2-week sprint—requirements specification,
traceability matrix, test logs, and decision rationale all
delivered automatically.
•Audit evidence:Documentation producedduringdevel-
opment, not weeks later. No separate compliance retrofit
required. Whether these artifacts satisfy a specific au-
ditor’s requirements depends on organizational controls,
scope, and regulatory context.
These gains are directionally consistent with the produc-
tivity improvements reported by Peng et al. [3] and McKin-
sey [29], while the Red Team Protocol addresses the quality
risks identified by He et al. [4] (Section II).
D. Sensitivity Analysis
The 25×cost reduction is based on specific assumptions.
To assess robustness, Table III varies the four key parameters
across pessimistic, baseline, and optimistic scenarios.
TABLE III
SENSITIVITYANALYSIS: COSTREDUCTIONFACTOR
Parameter Pessim. Base Optim.
Traditional effort 80 h 104 h 150 h
Labor rate (/hr) $100 $150 $200
Agile V human
hours
8 h 4 h 3 h
AI iteration cycles 3 1 1
Traditional cost$8,000 $15,600 $30,000
Agile V cost$830 $611 $608
Reduction factor 10×25×50×
Even under pessimistic assumptions (smaller project, lower
rates, triple the AI iterations), Agile V delivers a10×re-
duction; optimistic assumptions yield50×. The key structural
insight is thathuman time dominates the Agile V cost in all
scenarios—AI compute remains below 3% of total cost. A
10×increasein API pricing would raise the Agile V cost to
only $645, preserving a 24×reduction.
VI. RESULTS ANDDISCUSSION
This section evaluates the three hypotheses stated in Sec-
tion I. Table IV summarizes the evidence; the subsections
below discuss each hypothesis in detail.
A. H1: Audit-Evidence Artifacts as a By-Product
The Compliance Auditor agent produced six artifact types
as direct outputs of the engineering workflow: requirements
specification, traceability matrix (ATM.md), test execution log,
decision rationale document, risk register, and validation sum-
mary report. These are the core documents typically required
TABLE IV
HYPOTHESISEVALUATIONSUMMARY
Criterion Observed Verdict
H1 Audit-evidence arti-
fact set generated as
by-product
6 artifact
types produced
automatically
Supported
H2 100% req-level pass
rate, independent
tests
8/8 reqs, 54/54
tests (post-rework);
10 Red Team
findings caught
Supported∗
H3 Single-digit human
prompts per cycle
6 prompts/cycle, 2
model families
Supported
∗Requirement-level coverage only; mutation testing and branch-coverage
analysis were not performed.
for ISO 9001:2015 [20] design-control evidence and tradi-
tionally require 3–5 days of dedicated compliance effort per
project. Under Agile V, they were generated automatically
during Cycles 1 and 2 without a separate documentation phase.
Cycle 2 strengthened the evidence by addingmulti-cycle
traceability: everyTestResultand log entry carries acycle
identifier (e.g.,C1,C2), and the Artifact Traceability Ma-
trix tracks which requirements were added, modified, or un-
changed across cycles—providing auditors a complete change-
impact trail.
B. H2: Requirement-Level Verification
The project achieved a100% pass rate on 8 requirement-
level verification testsacross two cycles, with54 automated
testspassing after Cycle 2 rework (test-to-requirement ratio:
6.75:1). The suite covered both positive-path behaviour and
negative cases (e.g., exception handling for invalid inputs,
JSON round-tripping of thecyclefield). It didnotinclude
mutation testing, branch-coverage analysis, or fuzz testing; the
100% figure reflects requirement-level coverage, not exhaus-
tive code-level coverage. Readers should interpret these results
as a feasibility demonstration on a bounded system; whether
the approach scales to larger or more ambiguous projects is
an open question requiring independent replication.
The key design decision enabling this result is theRed
Team Protocol: the Build Agent and Test Designer operate
in parallel from thesame requirementsbut with no visibility
into each other’s output. This structural separation eliminates
“success bias”—the failure mode where tests only verify what
the code happens to do rather than what itshoulddo.
Cycle 2 provides concrete evidence: the Red Team Verifier
identified10 findings(6 MAJOR, 4 MINOR), including stale
API references after refactoring, missing field propagation, an
async property anti-pattern, and input validation gaps. These
10 findings represent thefirst-pass defect rateof the Build
Agent’s output—the quality signal that the iterative correction
mechanism is designed to surface. All MAJOR findings were
resolved in a single rework pass, yielding convergence in
one iteration for this bounded scope. More complex domains
should be expected to require additional iterations; tracking

# Extracted page 7

first-pass defect rates across projects would provide a useful
benchmark for future evaluations.
C. H3: Minimal Human Interaction
Each cycle required only6 human prompts: providing
initial intent, approving at Gate 1, directing synthesis, and
approving at Gate 2. The engineer contributed≈10% of ar-
chitecture decisions; the remaining effort was agent-generated.
Based on tool-call analysis, approximately 40% of agent
activity was code generation; the remaining 60% was planning,
verification, compliance documentation, and orchestration.
The two cycles used different AI model families (Gem-
ini 1.5 Pro in Cycle 1, Claude Opus 4.6 in Cycle 2), providing
initial evidence that the prompt count is framework-determined
rather than model-dependent. However, agent behaviour and
output quality may still vary across models (Section VI-E).
D. Regulatory Alignment
Table V presents adesign-time analysismapping
ISO 9001:2015 [20] clauses to Agile V mechanisms.
These mappings have not been validated by a third-party
auditor.
TABLE V
MAPPING OFAGILEVTOISO 9001:2015 CLAUSES
Clause Requirement Agile V Mechanism
4.4 QMS and its processes Infinity Loop defines repeat-
able, measurable processes
7.5 Documented
information
Compliance Auditor
auto-generates controlled
documents
8.3.4 Design controls Human Gates 1 and 2 enforce
review and approval
8.5.2 Identification and trace-
ability
Traceability Matrix links REQ
→Code→Test
9.1 Monitoring and mea-
surement
Red Team Verifier provides
objective test evidence
10.2 Nonconformity / correc-
tive action
Infinity Loop feeds failures
back for re-synthesis
Cycle 2 provides direct evidence for Clause 10.2: CR-
0001 triggered 10 nonconformity findings resolved in a single
corrective-action pass. The Infinity Loop also maps struc-
turally toISO 13485:2016[30] design and development
controls (design inputs via Requirement Architect, verifica-
tion via Red Team, validation via Human Gate 2) and to
ISO/IEC 27002:2022[31] separation of duties through the
Human Gates.
E. Threats to Validity
Several limitations constrain the generalizability of the
results presented in this paper:
•Single case study (external validity):One HIL project
with bounded complexity; results may not generalize
to large-scale systems with ambiguous requirements or
multi-team coordination. Independent replication on di-
verse project types is needed.
•Author evaluation (construct validity):The framework
was evaluated by its creators, introducing potential bias.
Third-party evaluations would strengthen the evidence
base.
•Model dependency:Two frontier models were used
(Gemini 1.5 Pro, Claude Opus 4.6), providing cross-
family evidence, but agent behavior and quality may vary;
the 100% pass rate should not be assumed universal.
•Cost comparison scope:The Agile V cost excludes
one-time adoption overhead; the traditional baseline is
estimated rather than observed. Both could narrow the
reported gap.
•Test depth:54 automated tests validated functional
requirements but excluded mutation testing, fuzz test-
ing, and formal verification. The 100% figure reflects
requirement-level, not code-level, coverage.
For GMP/GxP-regulated industries [32]–[34], the Infinity
Loop maps to GAMP 5 Category 5: the Requirement Architect
produces URS-level specifications, the Build Agent produces
design specifications, and the Red Team Verifier provides
IQ/OQ/PQ-equivalent evidence—with the Traceability Ma-
trix linking DS→FS→URS. ALCOA+ data integrity
is supported through attributable artifacts, contemporaneous
timestamped logs, and version-controlled primary records.
VII. CONCLUSION
This paper introduced Agile V, a framework that embeds
independent verification and audit artifact generation into each
AI-assisted task cycle. We evaluated three hypotheses through
a Hardware-in-the-Loop case study spanning two Infinity Loop
cycles.
H1 (Audit-Evidence By-Product): Supported.The Com-
pliance Auditor agent automatically generated a requirements
specification, traceability matrix, test execution logs, and de-
cision rationale document as direct outputs of the engineering
workflow—artifacts that typically require 3–5 days of dedi-
cated compliance effort.
H2 (Verification Pass Rate): Supported.The Red Team
Protocol’s structural separation between Build Agent and Test
Designer yielded 100% requirement-level pass rate across
8 requirements and 54 tests. Cycle 2’s Red Team findings
(10 issues, all resolved) demonstrate the protocol’s ability to
catch and correct defects through independent verification.
H3 (Minimal Human Interaction): Supported.Each
cycle required only 6 human prompts while maintaining full
traceability across cycles and across two different AI model
families (Gemini 1.5 Pro and Claude Opus 4.6).
These results support the hypothesis that Agile V addresses
the gap in current AI-assisted workflows: the framework
achieved an estimated 10–50×cost reduction versus a
COCOMO II baseline (Section V-D) while producing
structured audit-evidence documentation automatically. The
framework’s structural alignment with ISO 9001:2015 [20],
ISO 13485:2016 [30], ISO/IEC 27001:2022 [35],
ISO/IEC 27002:2022 [31], GAMP 5 [32], 21 CFR
Part 11 [33], and Annex 11 [34] supports auditability

# Extracted page 8

in regulated environments. Meeting these regulations in
production still requires validated system controls (e.g.,
access control, audit trails, record retention) beyond the
workflow artifacts reported here.
Limitations and Future Work.The evaluation is limited
to a single bounded project with well-defined interfaces, eval-
uated by the framework’s creators; independent replication on
diverse project types by external teams is essential for external
validity. The ISO compliance mappings require third-party
auditor validation. Integrating mutation testing and formal
verification into the Red Team Protocol would strengthen con-
fidence beyond requirement-level coverage. Finally, Wright’s
Law [36], [37] predicts continued AI inference cost declines;
as compute becomes asymptotically negligible, organizations
could affordmoreverification cycles per task, further widening
the framework’s cost advantage.
Agile V is published as an open standard (CC BY-SA 4.0) at
https://agile-v.org; a replication package (requirements, trace-
ability matrix, test suite, Red Team report, session logs) is
available in the project repository. The competitive advantage
will not go to organizations that generate code fastest, but to
those that canverify and shipfastest.
ACKNOWLEDGMENTS
The authors thank Philipp Rosendahl and Lukas Blocher for
their thorough review of the manuscript and valuable feedback.
AI Tool Usage Disclosure
In accordance with arXiv policy, we disclose the following
use of generative AI tools in the preparation of this work.
The case study (Section IV) was executed using commercial
AI platforms (Gemini 1.5 Pro and Claude Opus 4.6) as de-
scribed in Section IV-B; these tools generated source code, test
suites, and compliance documentation as part of the Agile V
workflow under evaluation. AI writing assistants were used for
drafting and editing portions of this manuscript. The authors
reviewed, verified, and take full responsibility for all content.
This paper is licensed under the Creative Commons Attribution 4.0 In-
ternational License (CC BY 4.0). To view a copy of this license, visit
https://creativecommons.org/licenses/by/4.0/. The Agile V standard and skills
library are separately licensed under CC BY-SA 4.0.
REFERENCES
[1] F. Dell’Acqua, E. McFowland III, E. R. Mollick, H. Lifshitz-Assaf,
K. Kellogg, S. Rajendran, L. Krayer, F. Candelon, and K. R. Lakhani,
“Navigating the jagged technological frontier: Field experimental ev-
idence of the effects of AI on knowledge worker productivity and
quality,”Harvard Business School Working Paper 24-013, 2023.
[2] Stack Overflow, “AI — 2025 Stack Overflow developer survey,” https:
//survey.stackoverflow.co/2025/ai, 2025, accessed: 2026-02-23.
[3] S. Peng, E. Kalliamvakou, P. Cihon, and M. Demirer, “The impact of
AI on developer productivity: Evidence from GitHub Copilot,”arXiv
preprint arXiv:2302.06590, 2023.
[4] H. He, C. Miller, S. Agarwal, C. Kästner, and B. Vasilescu, “Speed at
the cost of quality: How Cursor AI increases short-term velocity and
long-term complexity in open-source projects,” inProceedings of the
23rd International Conference on Mining Software Repositories (MSR
’26), 2026.
[5] B. Fitzgerald, K.-J. Stol, R. O’Sullivan, and D. O’Brien, “Scaling agile
methods to regulated environments: An industry case study,” inPro-
ceedings of the 35th International Conference on Software Engineering
(ICSE ’13). IEEE, 2013, pp. 863–872.
[6] A. Poth, H. Jacobsen, and A. Riel, “A systematic approach to agile
development in highly regulated environments,” inAgile Processes in
Software Engineering and Extreme Programming Workshops (XP 2020
Workshops), ser. Lecture Notes in Business Information Processing, vol.
396. Springer, 2020, pp. 111–119.
[7] O. Ojameruaye and R. Bahsoon, “Systematic elaboration of compliance
requirements using compliance debt and portfolio theory,” inRequire-
ments Engineering: Foundation for Software Quality (REFSQ 2014),
ser. Lecture Notes in Computer Science, vol. 8396. Springer, 2014, pp.
152–167.
[8] N. Harvey and D. DeBellis, “Highlights from the 10th
DORA report,” https://cloud.google.com/blog/products/devops-sre/
dora-2024-software-development-trends, 2024, published: 2024-10-23;
Accessed: 2026-02-23.
[9] A. Bacchelli and C. Bird, “Expectations, outcomes, and challenges
of modern code review,” inProceedings of the 35th International
Conference on Software Engineering (ICSE ’13). IEEE, 2013.
[10] K. Schwaber and J. Sutherland,The Scrum Guide. Scrum.org, 2020.
[11] K. Forsberg, H. Mooz, and H. Cotterman,Visualizing Project Manage-
ment: Models and Frameworks for Mastering Complex Systems, 3rd ed.
John Wiley & Sons, 2005.
[12] C. Koch and J. A. Wellbrock, “Agile v: A new open standard for ai-
augmented engineering,” https://agile-v.org, 2026, accessed: 2026-02-20.
[13] Agile-V .org, “Agile v skills repository (v1.3),” https://github.com/
Agile-V/agile_v_skills, 2026, v1.3; includes context engineering pat-
terns adapted from GSD (MIT License). Accessed: 2026-02-21.
[14] A. Spillner, “The W-Model: Strengthening the bond between devel-
opment and test,” inProceedings of the International Conference on
Software Testing, Analysis and Review (STAR East), Orlando, FL, 2002.
[15] Scaled Agile, Inc., “Scaled agile framework (SAFe) 6.0,” https://
scaledagileframework.com, 2024, accessed: 2026-02-20.
[16] H. Myrbakken and R. Colomo-Palacios, “DevSecOps: A multivocal
literature review,” inSoftware Process Improvement and Capability
Determination (SPICE 2017), ser. Communications in Computer and
Information Science, vol. 770. Springer, 2017, pp. 17–29.
[17] C. Lemieux, J. P. Inala, S. K. Lahiri, and S. Sen, “CodaMosa: Escaping
coverage plateaus in test generation with pre-trained large language mod-
els,” inProceedings of the 45th International Conference on Software
Engineering (ICSE ’23). IEEE, 2023, pp. 919–931.
[18] Z. Chen, S. Wang, Y . Zhou, S. Deng, C. Liu, and J. Gu, “ChatU-
niTest: A framework for LLM-based test generation,”arXiv preprint
arXiv:2305.04764, 2024.
[19] L. Christopherson, “Get shit done (GSD): A meta-prompting and context
engineering system for AI coding agents,” https://github.com/gsd-build/
get-shit-done, 2025, mIT License; Accessed: 2026-02-21.
[20]ISO 9001:2015 Quality management systems — Requirements, Interna-
tional Organization for Standardization Std., 2015.
[21] P. Lewis, E. Perez, A. Piktus, F. Petroni, V . Karpukhin, N. Goyal,
H. Küttler, M. Lewis, W.-t. Yih, T. Rocktäschel, and S. Riedel,
“Retrieval-augmented generation for knowledge-intensive NLP tasks,”
arXiv preprint arXiv:2005.11401, 2020.
[22] C. Packer, V . Fang, S. Patil, K. Lin, S. Wooders, and J. E. Gonza-
lez, “MemGPT: Towards LLMs as operating systems,”arXiv preprint
arXiv:2310.08560, 2023.
[23]Saleae Logic 2 Automation API Documentation, https://saleae.github.io/
logic2-automation/, Saleae, Inc., 2026, accessed: 2026-02-20.
[24] B. Boehm, C. Abts, A. W. Brown, S. Chulani, B. K. Clark, E. Horowitz,
R. Madachy, D. J. Reifer, and B. Steece,Software Cost Estimation with
COCOMO II. Prentice-Hall, 2000.
[25] The Standish Group, “CHAOS report 2015,” The Standish Group
International, Inc., Tech. Rep., 2015.
[26] Anthropic, “Anthropic API pricing,” https://docs.anthropic.com/en/docs/
about-claude/pricing, 2026, accessed: 2026-02-23.
[27] Google, “Gemini API pricing,” https://ai.google.dev/pricing, 2026, ac-
cessed: 2026-02-23.
[28] OpenAI, “Openai API pricing,” https://openai.com/api/pricing/, 2026,
accessed: 2026-02-23.
[29] McKinsey Global Institute, “The economic potential of generative AI:
The next productivity frontier,” McKinsey & Company, Tech. Rep.,
2023.

# Extracted page 9

[30]ISO 13485:2016 Medical devices — Quality management systems —
Requirements for regulatory purposes, International Organization for
Standardization Std., 2016.
[31]ISO/IEC 27002:2022 Information security, cybersecurity and privacy
protection — Information security controls, International Organization
for Standardization Std., 2022.
[32] International Society for Pharmaceutical Engineering,GAMP 5: A Risk-
Based Approach to Compliant GxP Computerized Systems, 2nd ed.
ISPE, 2022, gAMP 5 Second Edition.
[33]21 CFR Part 11: Electronic Records; Electronic Signatures, U.S. Food
and Drug Administration Std., 2003, current as of 2024.
[34]EudraLex Volume 4, Annex 11: Computerised Systems, European Com-
mission Std., 2011, gMP Guidelines.
[35]ISO/IEC 27001:2022 Information security, cybersecurity and privacy
protection — Information security management systems — Require-
ments, International Organization for Standardization Std., 2022.
[36] T. P. Wright, “Factors affecting the cost of airplanes,”Journal of the
Aeronautical Sciences, vol. 3, no. 4, pp. 122–128, 1936.
[37] K. F. Pilz, L. Heim, and N. Brown, “Increased compute efficiency and
the diffusion of AI capabilities,” inProceedings of the AAAI Conference
on Artificial Intelligence, 2025.
