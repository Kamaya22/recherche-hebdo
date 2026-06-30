# CRISPR and Genome Editing Therapies — Day 2/7: Panorama — From Bacterial Immunity to the First Approved Gene-Editing Medicine

## Context

This is the opening reading of a new week-long deep dive into CRISPR and genome editing therapies. The week was picked up mid-course (no Day 1 was produced), so today's reading doubles as a panorama: it lays out the core concepts, the molecular machinery, and the landmark clinical milestone — the FDA approval of Casgevy in December 2023 — that makes this week's theme worth a full week of attention.

CRISPR stands for Clustered Regularly Interspaced Short Palindromic Repeats. The name describes a peculiar pattern in the genomes of bacteria that microbiologists began noticing in the 1980s but did not fully understand until the 2000s: short, identical DNA sequences repeated at regular intervals, with unique "spacer" sequences sandwiched between them. Those spacers turned out to be fragments of viral DNA — a molecular immune memory that bacteria use to recognize and destroy viruses they have fought before. The Cas proteins associated with CRISPR arrays are the effectors: RNA-guided molecular scissors that find viral DNA by matching it to the stored spacer and cut it. In 2012, Jennifer Doudna, Emmanuelle Charpentier, and their teams demonstrated that the Cas9 protein could be reprogrammed with a synthetic guide RNA to cut any DNA sequence you wanted. The Nobel Prize in Chemistry followed in 2020. In 2013, Feng Zhang's laboratory showed the system works in human cells. Less than twelve years later, the first therapy built on this bacterial immune mechanism entered clinical use.

The rest of the week will unpack each major dimension in turn: delivery (Day 3), the anatomy of Casgevy (Day 4), the clinical pipeline (Day 5), safety and next-generation editing tools (Day 6), and ethics and governance (Day 7). Today's job is to ensure you have the mechanistic foundation — so that "BCL11A enhancer disruption" and "fetal hemoglobin reactivation" are not just jargon but a legible causal chain.

## Today's readings (~22 min total)

**1. CRISPR/Cas9 therapeutics: progress and prospects** — Xu, Yin, et al. (*Signal Transduction and Targeted Therapy*, Nature Publishing Group, 2023)
<https://www.nature.com/articles/s41392-023-01309-7>
*Estimated reading time: 12 min (abstract + Introduction + Sections 1–3 on mechanism, delivery overview, and clinical applications)*

A comprehensive peer-reviewed review published in a high-impact Nature-family journal, covering the CRISPR-Cas9 system from molecular mechanism through delivery strategies to clinical progress. The review synthesizes hundreds of primary studies and is written for an educated non-specialist scientific audience. It provides the clearest unified account of how Cas9 finds its target, why PAM recognition matters, and where the clinical pipeline stood at the time of publication. Signal Transduction and Targeted Therapy is indexed in PubMed and Web of Science, with an impact factor placing it among the top biomedical journals.

**2. Exagamglogene Autotemcel for Severe Sickle Cell Disease** — Frangoul, Locatelli, Sharma, et al. (*New England Journal of Medicine*, 2024)
<https://www.nejm.org/doi/full/10.1056/NEJMoa2309676>
*Estimated reading time: 8 min (abstract + Patient Characteristics + Efficacy Results + Discussion)*

The Phase 3 clinical trial paper that provided the primary evidence for the FDA's December 2023 approval of Casgevy for sickle cell disease. The NEJM is the world's highest-impact general medical journal; this paper provides the full efficacy and safety data from the CLIMB-SCD-121 trial, with 29 patients and a median follow-up of 19.3 months. Reading this alongside the review gives you the direct connection between the molecular mechanism described in source 1 and the patient outcomes it enables.

**3. Mechanism and Applications of CRISPR/Cas-9-Mediated Genome Editing** — (PMC review, 2021)
<https://pmc.ncbi.nlm.nih.gov/articles/PMC8388126/>
*Estimated reading time: 5 min (abstract + sections on PAM recognition, NHEJ vs. HDR)*

A focused peer-reviewed review on the mechanics of Cas9 action, freely accessible via PubMed Central. Particularly useful for the section comparing NHEJ and HDR outcomes, which is essential background for understanding why the choice between gene knockout (NHEJ) and gene correction (HDR) matters clinically. Short and technically precise; a good complement to the broader review in source 1.

## Guided summary (~8 min)

**How the molecular machine works**

The CRISPR-Cas9 editing system has two components. The first is the Cas9 protein itself — an enzyme about 1,400 amino acids long with two nuclease domains called HNH and RuvC, which independently cut the two strands of the DNA double helix. The second is a single guide RNA (sgRNA): a short synthetic molecule with a 20-nucleotide "spacer" sequence that is designed to be complementary to the DNA target, attached to a structural scaffold that holds Cas9 in the right conformation. You program the system to cut a new genomic location simply by synthesizing a new 20-nucleotide spacer — no protein re-engineering required. This simplicity is what made CRISPR transformative: earlier programmable nucleases (zinc fingers, TALENs) required designing a new protein for every new target; CRISPR reduced the problem to writing an RNA sequence.

The Cas9-sgRNA complex searches for its target by diffusing along DNA and pausing at specific short sequences called PAM (Protospacer Adjacent Motif) sites. For the most widely used Cas9 (from *Streptococcus pyogenes*), the PAM is the three-letter sequence 5'-NGG-3'. Cas9 first recognizes the PAM, then partially unwinds the adjacent DNA and tests whether the exposed strand matches the guide RNA. If the 20-nucleotide spacer anneals to the unwound DNA with sufficiently high complementarity, the system locks into an active conformation: the HNH domain cuts the strand matching the guide, and RuvC cuts the opposite strand. The result is a blunt-ended double-strand break (DSB) at a precise location in the genome — typically 3 base pairs upstream of the PAM.

**What happens to the broken DNA**

The cell immediately detects a DSB as a crisis and mobilizes repair machinery. There are two main routes. Non-Homologous End Joining (NHEJ) simply glues the broken ends back together — fast, active throughout the cell cycle, but error-prone. The repair machinery frequently introduces small insertions or deletions (indels) at the junction. If the break is in a protein-coding gene, these indels shift the reading frame and introduce a premature stop codon, effectively knocking out the gene. NHEJ is the tool of choice when the therapeutic goal is to disrupt a gene (for example, disrupting a viral receptor, or eliminating a transcription factor that silences a beneficial gene).

The second pathway, Homology-Directed Repair (HDR), uses a template — a piece of DNA with sequences homologous to the region flanking the break — to guide precise repair. HDR can correct a disease-causing mutation to the healthy sequence, or insert an entirely new sequence. The trade-off is that HDR is only active during the S and G2 phases of the cell cycle, when the cell is copying its DNA, and even then is slower and less frequent than NHEJ. In proliferating cells in culture, HDR can be achieved with good efficiency; in non-dividing cells in living tissue, it remains very difficult to trigger. This is why most current CRISPR therapies use NHEJ-based strategies (disruption) rather than HDR-based correction, even when correction would be the more obvious fix.

**The BCL11A insight: a detour through fetal hemoglobin**

Understanding how Casgevy works requires a short excursion into developmental biology. Sickle cell disease (SCD) is caused by a single point mutation in the beta-globin gene (HBB): an A-to-T change that replaces glutamate with valine at position 6 of the beta-globin protein. The mutant protein tends to polymerize when deoxygenated, distorting red blood cells into the characteristic sickle shape that blocks small blood vessels (vaso-occlusive crises) and shortens red cell lifespan. Beta-thalassemia involves a variety of mutations that reduce or eliminate beta-globin production, leading to chronic anemia.

An important biological fact has been known for decades: fetuses use a different hemoglobin — fetal hemoglobin (HbF), made from the HBG1 and HBG2 genes — that doesn't contain the sickle mutation or depend on beta-globin. HbF is switched off after birth and replaced by adult hemoglobin. Clinicians noticed that patients who happen to carry mutations that prevent this switch — a condition called hereditary persistence of fetal hemoglobin (HPFH) — are largely protected from the worst effects of SCD, because HbF can substitute for the defective adult hemoglobin. If you could reactivate HbF production in an adult patient, you might effectively cure the disease.

The transcription factor BCL11A is the master switch. In adult erythroid (red blood cell precursor) cells, BCL11A binds to regulatory regions near the HBG1/HBG2 genes and silences them. BCL11A itself is controlled in part by an erythroid-specific enhancer — a regulatory element that is active only in red cell precursors. Disrupting this enhancer with CRISPR-Cas9 reduces BCL11A expression specifically in the erythroid lineage without broadly affecting BCL11A's roles in other tissues (where it remains essential). The result: HGG1/HBG2 are de-repressed, HbF is produced in large quantities in red blood cells, and the pathological effects of the beta-globin mutation are overcome.

**The CLIMB trials and FDA approval**

Casgevy (developed by CRISPR Therapeutics and Vertex Pharmaceuticals) implements this strategy ex vivo: blood stem cells (CD34+ hematopoietic stem and progenitor cells) are collected from the patient through apheresis, edited with Cas9-sgRNA targeting the BCL11A erythroid enhancer in the laboratory, and then infused back after the patient undergoes myeloablative conditioning (high-dose busulfan chemotherapy to clear the bone marrow and make room for the edited cells). The edited cells engraft in the marrow and generate red blood cell precursors with disrupted BCL11A enhancers — and therefore high fetal hemoglobin — for the rest of the patient's life, theoretically.

In the Phase 3 CLIMB-SCD-121 trial published in the NEJM (2024), 29 patients with severe SCD received Casgevy. The results were striking: **96.7% of patients (28 out of 29) were free of severe vaso-occlusive crises for at least 12 consecutive months**, and **100% were free of SCD-related hospitalizations** over the same period. Bone marrow and blood samples showed approximately 80% allele editing with no evidence of off-target cutting at detectable levels. In the companion beta-thalassemia trial (CLIMB-Thal-111), more than 90% of patients achieved transfusion independence — meaning they no longer needed the regular blood transfusions that are a lifelong burden for severe TDT patients.

The FDA approved both indications in December 2023, making Casgevy the first CRISPR-based medicine ever authorized for human use. The European Medicines Agency and UK MHRA had approved it slightly earlier that same month.

**What this does and doesn't prove**

Casgevy's approval is a proof of concept for an entire therapeutic modality, not just one drug. It demonstrates that (a) CRISPR-Cas9 can achieve clinically meaningful levels of editing in human hematopoietic stem cells, (b) the edited cells can durably engraft and function in patients, (c) the BCL11A-HbF reactivation strategy translates to dramatic symptom relief, and (d) the off-target safety profile is manageable at current detection limits. These validations will benefit every other CRISPR therapy in development.

At the same time, Casgevy's success comes with important caveats. The ex vivo + myeloablation approach works for blood-forming stem cells because those cells can be collected, edited outside the body, and transplanted — but it cannot be applied to diseases of the brain, heart, or lung in the same way. The myeloablative conditioning is itself toxic, carrying risks of infertility, infections, and secondary malignancies. And the therapy is priced at approximately $2.2 million per patient, raising immediate questions about who can actually access it. The clinical breakthrough is real and large; the translational and equity challenges are equally real.

## Questions to think about

1. Casgevy uses NHEJ to disrupt the BCL11A enhancer — an indirect strategy (silence the silencer) rather than directly correcting the underlying HBB mutation via HDR. Why might the indirect approach work better in practice even though direct correction would seem more elegant? What does this tell us about the constraints that currently govern therapeutic gene editing choices?

2. The ex vivo approach — extracting cells, editing them outside the body, then re-infusing — works for blood stem cells but not for many other tissues. As you think ahead to diseases like Huntington's (brain) or Duchenne muscular dystrophy (muscle), what delivery and targeting challenges would need to be solved? (We'll address this in Day 3.)

3. Casgevy costs $2.2 million for a one-time treatment. SCD disproportionately affects people of African and Middle Eastern descent, populations with high rates of poverty globally. Does the usual pharmaceutical pricing logic — recouping R&D costs over a patient population — apply well here? What alternative models might be needed?
