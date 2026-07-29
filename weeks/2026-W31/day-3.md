# Quantum computing for the non-physicist — Day 3/7: Quantum Gates and Circuits — The Language of Quantum Algorithms

## Context (2–3 paragraphs)

The first two days built the foundations: Day 1 gave us the wide-angle panorama — superposition, entanglement, and interference as the three pillars of quantum computation, and the lay of the land between NISQ devices and the fault-tolerant machines of the future. Day 2 zoomed in on a single qubit: the Bloch sphere as a geometric map of quantum states, T₁ and T₂ as the two timescales of decoherence, and the precise physical reason why superconducting quantum processors must be cooled to 15 millikelvin. Today we take the next step: from individual qubits to quantum *circuits* — the structured sequences of operations that turn isolated quantum phenomena into algorithms.

The key mental shift for today is to think of a quantum computation as a piece of music scored for a small ensemble. Each instrument (each qubit) plays a sequence of notes according to its part; the score specifies exactly when each player acts and how the players coordinate. A quantum circuit is this score: a diagram with one horizontal wire per qubit, and gates — each representing a precisely defined mathematical operation — arranged in columns that are executed in order from left to right. The gates are the notes; the wires are the instrumentalists; the interference between their combined amplitudes is what produces a meaningful final chord instead of random noise.

This session connects Day 2's physics to Day 4's algorithms. We will see how individual qubit rotations are catalogued into a standard toolkit of named gates, how two-qubit gates like the CNOT create entanglement, what makes a set of gates *universal* (meaning sufficient to approximate any possible quantum algorithm), and how the cost of a quantum algorithm is measured in circuit depth. By the end of today you will be able to read a quantum circuit diagram and understand why one circuit can solve a problem faster than any classical algorithm — not through magic, but through a precise engineering of constructive and destructive interference.

## Today's readings (2–3 items, ~20 min total)

**1. "Guest Column: An introduction to quantum information and quantum circuits"** — Watrous, J. — *ACM SIGACT News* (Association for Computing Machinery), vol. 42, no. 2, pp. 52–67 (June 2011) — <https://dl.acm.org/doi/pdf/10.1145/1998037.1998053> — ~12 min (read sections 1–4 on quantum states, quantum circuits, and circuit diagrams) — This guest column was written for *SIGACT News*, the ACM Special Interest Group on Algorithms and Computation Theory's flagship newsletter, by John Watrous of the Institute for Quantum Computing at the University of Waterloo. Watrous is one of the most influential quantum information theorists working today, co-author of the leading textbook on the theory of quantum information, and the lecturer of the IBM Quantum Learning series on quantum information science. The paper introduces the circuit model precisely but accessibly: what wires and gates mean, how circuits are read, and what universality of quantum gate sets requires. ACM *SIGACT News* is the leading professional publication in theoretical computer science.

**2. "Quantum Computing in the NISQ era and beyond"** — Preskill, J. — *Quantum* (Verein zur Förderung des Open Access Publizierens in den Quantenwissenschaften), vol. 2, article 79 (August 2018) — <https://quantum-journal.org/papers/q-2018-08-06-79/> — ~8 min (read the sections on what NISQ circuits can do, circuit depth, and gate fidelity) — This highly cited paper (over 6,000 citations as of 2025) by John Preskill — Caltech professor who coined the term "quantum supremacy" and named the NISQ era — explains how circuit depth and gate fidelity together determine which computations are feasible on near-term hardware. The passage from "a quantum circuit with this many gates" to "here is how much noise accumulates" is explained clearly enough for a non-specialist to follow. *Quantum* is a peer-reviewed open-access journal operated as a non-profit community effort by the quantum information science community; all articles are published under a Creative Commons CC BY 4.0 licence.

**3. "Quantum Supremacy Is Coming: Here's What You Should Know"** — Hartnett, K. — *Quanta Magazine*, July 18, 2019 — <https://www.quantamagazine.org/quantum-supremacy-is-coming-heres-what-you-should-know-20190718/> — ~5 min — This accessible article by *Quanta Magazine* staff writer Kevin Hartnett explains, for a general audience, what quantum circuits are, why circuit depth and width matter, and what quantum supremacy means in concrete terms. It uses Google's then-imminent random circuit sampling experiment as a hook to explain why the *size* of a quantum circuit — counted in gates applied to qubits — determines what a machine can do. *Quanta Magazine* is an editorially independent publication of the Simons Foundation, staffed by professional science journalists and edited by researchers; its quantum computing coverage is regularly cited in policy and academic contexts as a reliable secondary source.

## Guided summary (~8 min)

### Quantum gates as unitary matrices: every operation is reversible

In classical digital computing, logic gates like AND, OR, and NAND are not generally reversible: knowing the output of an AND gate does not tell you the inputs (there are three input combinations that produce output 0). Quantum gates are fundamentally different: every quantum gate is a *unitary* transformation. A unitary matrix U satisfies U†U = UU† = I (where U† is the conjugate transpose and I is the identity); this guarantees that the gate's inverse exists and equals U†. No information is lost, no state is irreversibly destroyed — until the moment of measurement.

On the Bloch sphere from Day 2, unitarity translates into geometry: every single-qubit gate corresponds to a *rotation* of the Bloch vector. This is not an analogy; it is an exact statement about the mathematics of SU(2) (the special unitary group in two dimensions). The same group describes rotations of a three-dimensional sphere. The angle and axis of rotation are what distinguish one gate from another. In quantum circuit diagrams, single-qubit gates are drawn as labelled boxes on the relevant qubit's wire; they are applied sequentially in left-to-right order.

### The standard single-qubit toolkit

A small vocabulary of named gates handles nearly all quantum algorithm design:

**X (the quantum NOT gate)**: a 180° rotation around the Bloch sphere's x-axis. It flips |0⟩ to |1⟩ and |1⟩ to |0⟩, exactly analogous to a classical NOT gate. The matrix is the first Pauli matrix: [[0, 1], [1, 0]].

**Z (the phase-flip gate)**: a 180° rotation around the z-axis. It leaves |0⟩ unchanged and multiplies |1⟩ by −1 (a phase factor). The matrix is [[1, 0], [0, −1]]. This gate does nothing to the *probability* of each outcome when measured in the computational basis — a state in superposition would yield the same probabilities before and after Z — but it changes the *phase relationship* between the amplitudes, which matters enormously in interference calculations.

**H (the Hadamard gate)**: a 180° rotation around the axis halfway between x and z — equivalently, the matrix (1/√2)[[1, 1], [1, −1]]. It takes the ground state |0⟩ to the equal superposition |+⟩ = (|0⟩ + |1⟩)/√2, and the excited state |1⟩ to the equal superposition |−⟩ = (|0⟩ − |1⟩)/√2. Applied to all n qubits of a register initialised in |00…0⟩, the Hadamard layer produces an equal superposition across all 2ⁿ computational basis states simultaneously — from |00…0⟩ to (|00…0⟩ + |00…1⟩ + … + |11…1⟩)/√(2ⁿ). This is the standard first step in nearly every quantum algorithm.

**S and T (phase rotation gates)**: the S gate is a 90° z-rotation, equivalent to the matrix [[1, 0], [0, i]]; T is a 45° z-rotation, [[1, 0], [0, e^(iπ/4)]]. These finer phase rotations are essential for controlling how amplitudes add and cancel during interference. Crucially, the T gate plays a special role in fault-tolerant circuit design, as will be explained below.

### The CNOT gate: entanglement from a two-qubit operation

No single-qubit gate can create entanglement; a gate acting on one qubit cannot produce correlations between two qubits. Entanglement requires two-qubit gates. The most important is the CNOT (Controlled-NOT):

- It acts on two qubits: a **control** qubit and a **target** qubit.
- Rule: if the control is in state |0⟩, the target is unchanged. If the control is in state |1⟩, the target is flipped (X is applied to it).
- On computational basis states: |00⟩ → |00⟩, |01⟩ → |01⟩, |10⟩ → |11⟩, |11⟩ → |10⟩.

Applied to computational basis states, CNOT looks like a classical operation (it reversibly copies the control's value into the target using XOR). The quantum leap occurs when the control is in a superposition. Consider: start with |0⟩⊗|0⟩, apply Hadamard to the first qubit, then CNOT:

1. After H on qubit 1: (|0⟩ + |1⟩)/√2 ⊗ |0⟩ = (|00⟩ + |10⟩)/√2
2. After CNOT: (|00⟩ + |11⟩)/√2

The result is the Bell state — the maximally entangled two-qubit state introduced in Day 1. If you measure one qubit, you instantly know the other's value. This two-gate sequence, H followed by CNOT, is the standard recipe for generating an entangled pair of qubits in any quantum circuit. All quantum algorithms that exploit entanglement use it at their core.

### Reading a quantum circuit diagram

A quantum circuit diagram follows a simple and consistent visual grammar:

- **Wires** are drawn as horizontal lines. Each wire represents one qubit. Wires are labelled on the left with the qubit's initial state (usually |0⟩).
- **Single-qubit gates** appear as labelled boxes (H, X, Z, S, T, …) on a single wire at the point in the circuit where they are applied.
- **CNOT** is drawn with a filled circle (•) on the control qubit's wire and a ⊕ symbol (direct sum) on the target qubit's wire, connected by a vertical line.
- **Time flows left to right**. Gates in the same vertical column are applied simultaneously (in parallel) to their respective qubits.
- **Measurement** is drawn as a meter symbol at the end of a wire, with a double line (classical bit) carrying the measurement outcome to the right.
- **Circuit width** is the number of qubits (the number of horizontal wires) — the *space* cost of a computation.
- **Circuit depth** is the length of the longest path from left to right, counted in gate layers — the *time* cost of a computation.

These two quantities — width and depth — together determine how expensive an algorithm is. A quantum computer with n physical qubits can execute circuits of width at most n. A quantum computer with decoherence time T₁ and gate time t_gate can execute circuits of depth at most roughly T₁/t_gate before decoherence degrades the result. From Day 2's numbers: T₁ ≈ 300 µs, t_gate ≈ 100 ns → maximum depth ≈ 3,000. That is a tight budget.

### Universal gate sets: the Clifford group and the T gate

A set of gates is called **universal** for quantum computing if every unitary transformation on any number of qubits can be approximated to arbitrary precision by circuits built from that set. Universality is the quantum analogue of the classical result that NAND gates alone can implement any boolean function.

The most important universal set in practice is {H, S, T, CNOT}. This is the **Clifford + T** gate set. To understand why this decomposition matters, we need to understand the Clifford group separately:

The **Clifford gates** are generated by H, S, and CNOT. They form a group (any circuit of Clifford gates can be composed into another Clifford gate) and have a remarkable property: Clifford circuits can be classically simulated efficiently, regardless of the number of qubits. This is not a failure — it is a feature. It means that Clifford circuits, despite being quantum, offer no computational advantage over classical computers. They are useful for quantum error correction (which requires classical simulation of the syndrome-measurement circuitry) but not for quantum speedup.

The gap is closed by the **T gate**. Adding T to the Clifford generators breaks the classical simulability: the set {H, S, T, CNOT} is universal, and circuits that use T gates cannot in general be simulated efficiently classically. The number of T gates in a circuit (its **T-count**) is therefore a key resource metric in fault-tolerant quantum computing, since T gates are far more expensive to implement in an error-corrected architecture than Clifford gates.

A fundamental theorem (the Solovay-Kitaev theorem) guarantees that any single-qubit gate can be approximated to within error ε using only O(log^c(1/ε)) gates from {H, S, T}, where c ≈ 2. This means no target gate is "out of reach" — the Clifford+T library is provably sufficient, with only polylogarithmic overhead for precision.

### Deutsch's algorithm: interference in action

The abstract framework of gates and universality comes to life in even the simplest quantum algorithm. Deutsch's algorithm (1985), though impractical in itself, is the template underlying every more powerful quantum algorithm:

**Problem**: You are given a boolean function f : {0, 1} → {0, 1}, implemented as a black box. You want to know whether f is *constant* (f(0) = f(1)) or *balanced* (f(0) ≠ f(1)). Classical answer: you must evaluate f at least twice. Quantum answer: one evaluation suffices.

The circuit uses two qubits — one "data" qubit and one "phase kickback" qubit:

1. Initialise: |0⟩⊗|1⟩
2. Apply H to both qubits: (|0⟩+|1⟩)/√2 ⊗ (|0⟩−|1⟩)/√2 = |+⟩⊗|−⟩
3. Apply the oracle Uf, which computes f in superposition: this "encodes" the function's value into the phase (sign) of the first qubit's amplitude, via a trick called **phase kickback**
4. Apply H to the first qubit
5. Measure the first qubit

If f is constant: the first qubit measures |0⟩ with certainty. If f is balanced: it measures |1⟩ with certainty. One query, definitive answer.

Why? The two passes through the Hadamard gate on the data qubit create conditions in which the amplitudes for "f is constant" interfere *constructively* at |0⟩ (amplitudes add) while the amplitudes for "f is balanced" interfere *destructively* at |0⟩ (amplitudes cancel) and constructively at |1⟩. This is quantum interference as a computational tool: the circuit is designed so that wrong answers cancel themselves out of the probability distribution, and only the correct answer survives to be measured.

All more powerful quantum algorithms — Shor's factoring (Day 4), Grover's search (Day 4), variational quantum algorithms — work by the same principle: they engineer a circuit in which the amplitude of the correct answer accumulates through constructive interference while all other amplitudes mutually cancel. The gates are the instruments; the circuit is the score; the interference is the music.

### Circuit depth and the NISQ constraint

Preskill's 2018 analysis makes the tension between circuit depth and hardware quality precise. The error probability per gate on the best current superconducting hardware is roughly 0.1–1% per two-qubit gate. A circuit of depth d applied to n qubits accumulates roughly d × n gate errors on average. If each gate has error probability p, the circuit's total success probability scales approximately as (1 − p)^(d×n). For p = 0.1% and d × n = 1,000, this gives (0.999)^1000 ≈ 37% success probability — borderline. For d × n = 10,000, it falls to (0.999)^10000 ≈ 5% — effectively useless without error mitigation.

This is why every NISQ-era algorithm is a race between the algorithm designer and the noise floor: can you do something computationally interesting — something classical computers cannot easily replicate — within the circuit depth budget that hardware noise allows? As of 2025-26, the answer is: perhaps, for a narrow class of quantum chemistry and optimization problems, but not yet for the landmark applications of cryptography or drug discovery. That gap will be closed — if it is closed — by the error correction techniques explored in Day 6.

## Questions to think about

1. The CNOT gate applied to a product state |+⟩⊗|0⟩ produces the entangled Bell state (|00⟩+|11⟩)/√2. Now suppose you apply CNOT to the product state |+⟩⊗|+⟩ = (|0⟩+|1⟩)/√2 ⊗ (|0⟩+|1⟩)/√2. Work through the computation: is the result entangled? What does this tell you about the relationship between superposition and entanglement — are all superpositions entangled, and are all entangled states superpositions?

2. The Clifford group is efficiently classically simulable (the Gottesman-Knill theorem), yet Clifford circuits include the Hadamard gate, the CNOT gate, and can produce highly entangled states like Bell states. This seems paradoxical: how can a circuit that creates genuine quantum entanglement be classically simulable? What is it about Clifford circuits specifically that makes them tractable for a classical computer, and what does the T gate break that restores classical computational hardness?

3. Circuit depth is constrained by gate error rates — the deeper the circuit, the more noise accumulates. But circuit depth can also be reduced by executing multiple gates in parallel on different qubits. If a hypothetical quantum algorithm requires 10,000 T gates applied in sequence (circuit depth 10,000, width 1 qubit) versus 1,000 T gates applied to 10 qubits in parallel (circuit depth 1,000, width 10), which circuit is easier to run on a NISQ device? What does this suggest about how algorithm designers should think about the width/depth trade-off given today's hardware?
