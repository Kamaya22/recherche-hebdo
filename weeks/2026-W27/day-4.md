# CRISPR and genome editing therapies — Day 4/7: Base editing and prime editing

## Context

Days 1 and 2 established that CRISPR-Cas9 works by creating a double-strand break (DSB) in DNA, and that the cell's subsequent repair of that break — through NHEJ (producing indels) or HDR (enabling precise correction with a template) — determines the editing outcome. Day 3 showed what this mechanism looks like in the clinic: Casgevy exploits NHEJ to disrupt the BCL11A erythroid enhancer, reactivating fetal hemoglobin; in vivo CRISPR approaches like nexiguran ziclumeran similarly use NHEJ to permanently knock out gene expression.

But DSB-mediated editing has intrinsic limitations. NHEJ can only disrupt genes efficiently; precise correction via HDR is inefficient in most therapeutically relevant cell types. More fundamentally, any approach that introduces a DSB has a non-zero risk of generating large chromosomal deletions, translocations, or — in rare cases — integration of unwanted DNA at the cut site. The vast majority of disease-causing mutations in the human genome are single nucleotide variants (SNVs): point mutations that swap one DNA letter for another. A tool that targets only DSBs is a blunt instrument for this category of disease.

Today we examine two technologies developed specifically to address this limitation: **base editing** and **prime editing**, both pioneered in David Liu's laboratory at the Broad Institute and Harvard University. Both make precise, defined changes at a target site without creating a double-strand break, and both have now entered clinical trials with striking early results.

## Today's readings (~22 min total)

**1. Programmable editing of a target base in genomic DNA without double-stranded DNA cleavage** — Komor, Kim, Packer, Zuris, Liu (*Nature*, 2016)
<https://www.nature.com/articles/nature17946>
*Estimated reading time: 7 min — abstract, introduction, the "Base Editors" section, and Figure 1*

Published in *Nature* on 20 April 2016 (doi:10.1038/nature17946), this paper introduced the first base editors — "CBEs," or cytosine base editors — capable of converting a C·G base pair to a T·A base pair in human cells without creating a DSB. The system works by fusing a catalytically impaired "nickase" Cas9 (nCas9, which cuts only one strand) to a cytidine deaminase enzyme (initially APOBEC1) that chemically converts cytosine to uracil within the R-loop formed during target DNA binding. The cell then reads the uracil as a thymine, and subsequent DNA replication permanently installs the C→T change. The paper reported editing efficiencies of up to 37% in human cells with minimal indels. This represents a conceptual step change: instead of relying on the cell's imprecise repair machinery after a DSB, the base editor performs a direct chemical conversion within the DNA, with the nick on the complementary strand serving only to bias mismatch repair toward the edited strand. Liu's laboratory subsequently developed adenine base editors (ABEs, 2017) for A·T→G·C conversions, giving the field a set of tools capable of making four of the twelve possible single-base transitions.

**2. Programmable base editing of A·T to G·C in genomic DNA without DNA cleavage** — Gaudelli, Komor, Rees, Packer, Badran, Liu (*Nature*, 2017)
<https://www.nature.com/articles/nature24644>
*Estimated reading time: 7 min — abstract, introduction, and Figure 1*

Published in *Nature* on 25 October 2017 (doi:10.1038/nature24644), this companion paper completed the base editing toolkit for transitions by introducing adenine base editors (ABEs). A→G (adenine to inosine, read as guanine) conversion does not occur in nature via a simple enzyme pathway in DNA, so Gaudelli, Komor, Rees, and colleagues had to evolve one: they used phage-assisted continuous evolution (PACE) to engineer a bacterial tRNA adenosine deaminase (TadA) to act on DNA within the R-loop created by a nickase Cas9. The resulting ABE7.10 converted A·T base pairs to G·C in human cells with up to 50% efficiency. Because A→G transitions account for nearly half of all known human pathogenic point mutations — including those underlying many cardiovascular risk genes, neurological conditions, and haematological disorders — ABEs dramatically expanded the therapeutic reach of precise editing. Subsequent generations (ABE8e, ABE8.20) have further improved efficiency and reduced off-target RNA editing.

**3. Search-and-replace genome editing without double-strand breaks or donor DNA** — Anzalone, Randolph, Davis, Sousa, Koblan, Levy, Chen, Wilson, Newby, Raguram, Liu (*Nature*, 2019)
<https://www.nature.com/articles/s41586-019-1711-4>
*Estimated reading time: 8 min — abstract, introduction, and the "Principle of Prime Editing" section with Figure 1*

Published in *Nature* on 21 October 2019 (doi:10.1038/s41586-019-1711-4), this paper introduced prime editing — described by the authors as a "search and replace" function for the genome. Prime editing uses a nickase Cas9 fused to an engineered reverse transcriptase, programmed by a "prime editing guide RNA" (pegRNA) that carries both the targeting sequence and, at its 3′ end, the encoded edit. After the nCas9 nicks the non-template strand, the pegRNA's 3′ extension hybridises to the nicked strand and serves as a template for the reverse transcriptase to copy the new sequence into the genome. The pasted edit is then resolved by the cell's mismatch repair machinery. In contrast to base editing, which is limited to transition mutations within a narrow editing window, prime editing can theoretically install any of the 12 types of point mutation, plus small insertions and deletions. The 2019 paper demonstrated over 175 different edits in human cells, including insertions up to 44 bases and deletions up to 80 bases. The technique is the most general precision editing system yet developed; its clinical development is slightly behind base editing but the first human trial (for chronic granulomatous disease) received FDA authorisation in 2024. The paper has been cited over 5,000 times in five years.

## Guided summary (~8 min)

**The problem base editing was designed to solve**

To appreciate why base editing matters, consider the arithmetic of human genetic disease. A 2019 analysis of pathogenic variants listed in ClinVar (the NIH's database of genetic variants) found that roughly 58% of disease-causing mutations in the database are single nucleotide variants. Of these, approximately 30% are C·G→T·A transitions — the most common class of point mutation, arising largely from spontaneous cytosine deamination — and a further 27% are A·T→G·C transitions. CBEs and ABEs together address these two classes. The remaining 43% — transversions, small indels, and other mutation types — require prime editing or classical CRISPR-HDR approaches.

The therapeutic implication is direct: sickle cell disease is caused by a single A·T→T·A transversion (a change that neither CBEs nor ABEs can correct). Casgevy therefore targets BCL11A to reactivate fetal hemoglobin rather than directly correcting the sickle mutation. But BEAM Therapeutics' BEAM-101 takes a different approach: it uses a CBE to introduce a point mutation into the HBG1 and HBG2 promoters that disrupts BCL11A binding, also reactivating fetal hemoglobin — achieving the same therapeutic end by a different and, importantly, DSB-free route.

**How CBEs and ABEs work: a conceptual comparison with Cas9**

A cytosine base editor (CBE) consists of three components: a nickase Cas9 (nCas9, D10A mutant that cuts only the non-target strand), a cytidine deaminase (APOBEC or AID family), and a UGI (uracil glycosylase inhibitor) to prevent the cell from excising the uracil before it can be read as thymine. When the nCas9-deaminase fusion binds the target site and forms an R-loop, a short segment of the target strand (typically ~5 bases corresponding to the "editing window" at positions ~4–8 counting from the PAM-distal end of the guide) is exposed as single-stranded DNA accessible to the deaminase. The deaminase converts C within this window to U; the nick on the non-target strand biases mismatch repair toward reading the edited strand as correct; and the result is a permanent C·G→T·A change. Fourth-generation CBEs (BE4max, AncBE4max) achieve up to 80% efficiency in some cell types with bystander editing rates (off-target Cs in the editing window) reduced to near zero.

Adenine base editors use the same architecture but with an evolved TadA enzyme replacing the deaminase, converting A within the editing window to I (inosine, read as G). Because adenosine deaminases that act on DNA do not exist in nature, the Liu laboratory used protein evolution (PACE and subsequent directed evolution) to create TadA variants with the desired activity. The 8th-generation ABE8e has become the most widely used ABE, achieving >80% efficiency at many target sites with off-target DNA editing below the detection threshold of standard assays.

**Prime editing: the most general precision tool**

Prime editing extends the precision of base editing to all 12 types of point mutation and small indels. Its core insight is to deliver both the cut and the new sequence template on a single RNA molecule — the pegRNA — which acts simultaneously as a guide (targeting the nCas9 to the right site) and as a template (encoding the desired edit at its 3′ end).

The mechanism proceeds in five steps: (1) the nCas9-reverse transcriptase fusion binds the target site via the pegRNA's spacer sequence; (2) the nCas9 nickase cuts the non-template strand at a defined position; (3) the 3′ extension of the pegRNA hybridises to the nicked strand via a primer-binding site; (4) the reverse transcriptase copies the edit-encoding sequence from the pegRNA into the nicked strand; (5) the resulting edit-containing sequence is resolved by the cell's mismatch repair (MMR) machinery. A secondary nick in the non-edited strand (using a separate standard sgRNA with the same nCas9) strongly improves efficiency by biasing MMR toward using the edited strand as the repair template.

Prime editing is generally less efficient than base editing for the mutations that both can address (typically 10–50% in human cells versus 40–80% for CBEs/ABEs), but it can correct or install sequences that base editing cannot touch. The two technologies are therefore complementary rather than competitive.

**First clinical results: base editing enters the clinic**

The first human clinical trial of a base-editing therapy began in 2021 when Great Ormond Street Hospital in London used CBE-edited allogeneic donor T-cells — cells base-edited to evade immune rejection and to target cancer — to treat a child with relapsed T-cell leukemia. That case demonstrated tolerability of base-edited cellular products in humans.

For monogenic blood diseases, BEAM Therapeutics' BEAM-101 is the first base-editing therapy in a randomised sickle cell disease trial. A 2025 paper in *The New England Journal of Medicine* (doi:10.1056/NEJMoa2504835) reported initial results from the BEACON Phase 1/2 study: all patients who received BEAM-101 achieved substantial fetal hemoglobin induction (>60% HbF as a fraction of total hemoglobin), with no vaso-occlusive crises reported after engraftment. BEAM-101 uses a CBE to introduce a point mutation in the HBG1/HBG2 promoters, disrupting BCL11A binding and reactivating the fetal hemoglobin switch. Like Casgevy, it requires ex vivo stem cell editing and myeloablative conditioning — the practical process is largely the same as the Cas9-based therapy.

VERVE Therapeutics has taken base editing in a different direction: VERVE-101 delivers an ABE in vivo via lipid nanoparticles to permanently edit the PCSK9 gene in the liver, knocking out the gene's expression and sharply reducing LDL cholesterol in patients with familial hypercholesterolemia. Early Phase 1 data reported in 2023 showed LDL reductions of up to 55%, with the effect appearing durable at 12 months. As of 2025, a Phase 2 randomised trial is underway.

**Prime editing in the clinic**

Prime editing's clinical translation has lagged base editing by approximately three years, reflecting the additional complexity of the pegRNA design, the lower initial efficiency, and the need to optimize delivery. The FDA authorised the first prime editing clinical trial in April 2024, for chronic granulomatous disease (CGD), a rare primary immunodeficiency caused by CYBB mutations. Prime Editors (the Liu laboratory spinout) is the lead developer. If the CGD trial succeeds, it will establish the clinical feasibility of the prime editing platform for a mutation class (a small deletion) that neither base editing nor Casgevy-type approaches can address.

## Questions to think about

1. CBEs and ABEs achieve higher efficiencies than prime editing for the mutation types they can address, but prime editing is more versatile. For a disease caused by a pathogenic single nucleotide variant that falls within base editing's capabilities, how would you decide between deploying a base editor (simpler, higher efficiency) and a prime editor (more complex, potentially more general)? What clinical and regulatory considerations would dominate?

2. All current ex vivo editing therapies for blood disorders — Casgevy, BEAM-101, and others — require myeloablative conditioning with busulfan before the edited cells are infused. This conditioning is toxic and carries irreversibility risks including infertility. What would it take to develop a conditioning-free approach, and how would that change the risk-benefit calculus for treating patients with mild-to-moderate disease severity (as opposed to patients with severe, life-threatening symptoms)?

3. Prime editing can install all 12 types of point mutation in human cells, including transversions that CBEs and ABEs cannot achieve. VERVE-101 and similar in vivo delivery platforms use lipid nanoparticles to deliver ABE mRNA to the liver. Could the same delivery platform in principle be used to deliver pegRNA-based prime editing therapeutics to non-hepatic organs, and what would be the key technical obstacles?

