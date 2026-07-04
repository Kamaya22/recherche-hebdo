# CRISPR and genome editing therapies — Day 5/7: Off-target effects and the safety science

## Context

The preceding four days of this week have mapped CRISPR-Cas9 from its bacterial immune origins (Day 1) through the molecular architecture that gives it precision (Day 2), into the clinic in the form of approved therapies for blood diseases (Day 3), and forward to next-generation tools that avoid double-strand breaks entirely (Day 4). Running alongside all of these advances is an uncomfortable question that surfaces in every regulatory submission, patient consent form, and clinical safety committee: what if Cas9 cuts somewhere it was not supposed to?

This is the off-target problem. It is not theoretical — off-target cleavage has been detected in cultured human cells with most guide RNAs tested at high enough sensitivity — but its clinical significance is a more nuanced question than it might seem. A cut in an intron of a non-essential gene is not the same as a cut in a proto-oncogene. A cut in a post-mitotic neuron (which will never divide again) carries different consequences than a cut in a hematopoietic stem cell that will generate millions of daughter cells over a lifetime. Understanding off-target risk requires understanding how off-target cleavage is detected, what the clinical safety data from approved and near-approved therapies actually show, and what the remaining scientific unknowns are.

Today also bridges to Day 6: the governance and ethics reading. Off-target safety is one of the key scientific arguments underlying the international consensus that germline editing — where any off-target event would be heritable — remains unacceptable at this time.

## Today's readings (~22 min total)

**1. GUIDE-seq enables genome-wide profiling of off-target cleavage by CRISPR-Cas nucleases** — Tsai, Zheng, Nguyen, Wilson, Hendel, Bhatt, Richardson, Szablowski, Liu, Reyon, Aryee, Joung (*Nature Biotechnology*, 2015)
<https://www.nature.com/articles/nbt.3117>
*Estimated reading time: 8 min — abstract, introduction, and the comparison of detection sensitivity with bioinformatic prediction*

Published in *Nature Biotechnology* in January 2015 (doi:10.1038/nbt.3117), this paper introduced GUIDE-seq (genome-wide, unbiased identification of DSBs enabled by sequencing) — the first method capable of detecting off-target CRISPR cuts across the entire genome without relying on computational prediction of likely mismatch sites. The method works by incorporating short double-stranded DNA oligonucleotides (dsODN "tags") into any double-strand break present in treated cells; the integration sites are then mapped by sequencing, revealing all genomic locations where Cas9 made a cut. GUIDE-seq demonstrated conclusively that the then-current understanding of off-target risk — based on in silico prediction of sequences similar to the guide — substantially underestimated actual cleavage activity: the method detected off-target sites that no existing prediction tool had identified. It also showed that off-target activity varies enormously across guide RNAs (some cutting hundreds of off-target sites, others only a handful), and that truncated guides (17–18 nt rather than 20 nt) could substantially reduce off-target activity at certain sites. GUIDE-seq became a standard element of clinical-grade off-target assessment and a reference method in both the Casgevy regulatory dossier and subsequent gene therapy evaluations. *Nature Biotechnology* is the leading applied biology journal; this paper has been cited over 4,000 times.

**2. Specificity of CRISPR-Cas9 Editing in Exagamglogene Autotemcel** — Sharma, Bhatt, Bhargava et al. (*New England Journal of Medicine*, 2024)
<https://www.nejm.org/doi/full/10.1056/NEJMc2313119>
*Estimated reading time: 7 min*

Published in *NEJM* on 9 May 2024, this correspondence reports the off-target analysis performed for exagamglogene autotemcel (exa-cel, Casgevy) — the first approved CRISPR therapy and therefore the first for which regulatory-grade off-target data in patients are publicly available. The authors describe a multi-layered approach: in silico screening of the entire human genome for sequences similar to the BCL11A enhancer guide RNA; GUIDE-seq analysis in human CD34+ cells; and orthogonal empirical methods. Importantly, the target site was deliberately chosen among candidate BCL11A enhancer guides to minimise sequence homology to any other site in the genome. The analysis found no off-target editing above the detection limit (~0.1%) at the ~30 in silico predicted top candidate sites. The piece is short (~2 pages) but is the most clinically relevant document currently available on CRISPR off-target safety in approved human therapeutics. The *New England Journal of Medicine* is the highest-circulation and most-cited clinical medicine journal in the world.

**3. Off-target effects in CRISPR-Cas genome editing for human therapeutics: Progress and challenges** — (*Molecular Therapy: Nucleic Acids*, 2025)
<https://www.cell.com/molecular-therapy-family/nucleic-acids/fulltext/S2162-2531(25)00190-8>
*Estimated reading time: 10 min — Abstract, "Current State of Off-Target Detection" section, and "Clinical Data and Regulatory Perspectives" section*

This 2025 review in *Molecular Therapy: Nucleic Acids*, published by Elsevier/Cell Press, provides the most current synthesis of the off-target detection landscape — covering GUIDE-seq, CIRCLE-seq, DISCOVER-seq, and newer methods — and critically evaluates the adequacy of current regulatory frameworks. It notes that Casgevy's approval relied on GUIDE-seq as its primary empirical method, while other recent therapies (reni-cel, NTLA-2001) have used multi-method approaches that improve sensitivity. The review also discusses the specific challenge of detecting chromosomal rearrangements (translocations between on-target and off-target sites), which standard sequencing-based methods may not capture efficiently. *Molecular Therapy* is the official journal of the American Society of Gene & Cell Therapy (ASGCT) and is among the most respected journals in the gene editing field.

## Guided summary (~8 min)

**The nature of off-target risk: what kinds of errors can Cas9 make?**

Off-target editing by CRISPR-Cas9 can manifest in several distinct ways, each with different clinical consequences.

The most commonly discussed form is *single-nucleotide off-target cleavage*: Cas9 binding and cutting at a genomic site whose sequence partially resembles the intended target, typically with 1–5 mismatches relative to the guide RNA. The probability of this occurring depends on both the guide RNA sequence (some sequences are inherently more promiscuous) and on cellular context (guide RNA concentration, Cas9 exposure time). GUIDE-seq revealed that some early guides had dozens of detectable off-target sites; modern guide design — incorporating computational specificity scoring, truncated guides, high-fidelity Cas9 variants, and empirical GUIDE-seq testing — has reduced this substantially for clinical-grade products.

A less-discussed but potentially more serious class of error is *chromosomal rearrangements*: translocations or inversions that occur when two DSBs (one on-target, one off-target) are simultaneously present in the same nucleus and their broken ends are joined by NHEJ in the wrong combination. Large deletions and copy-neutral inversions at the on-target site have also been detected at frequencies of 1–5% in some cell populations. These structural variants are generally not detected by standard amplicon-sequencing-based off-target assays, which focus on single-base-pair indels at predicted sites. Their clinical significance is unknown but potentially greater than point mutations.

A third class, primarily relevant to base editors and not standard Cas9, is *RNA off-target editing*: APOBEC and TadA deaminases fused to nCas9 may also edit transcribed RNAs in an sgRNA-independent manner, generating adenosine-to-inosine or cytidine-to-uridine changes in the transcriptome. While RNA editing is transient (mRNAs are degraded and resynthesised), high rates of RNA off-target activity could in principle affect cellular physiology. This concern has motivated the development of ABE variants (ABE8.20, RRECas9-based editors) with substantially reduced RNA off-target activity.

**Detection methods: a brief taxonomy**

Prior to 2015, off-target assessment relied almost entirely on bioinformatic prediction: identify the guide RNA sequence, search the genome for sequences with ≤3 mismatches, and empirically test those candidate sites by amplicon sequencing. This approach is fundamentally limited by its assumption that only sequences similar to the guide will be cut — an assumption that GUIDE-seq demonstrated was incorrect.

The post-2015 detection landscape is built around "unbiased" methods that discover off-target sites without prior prediction:

*GUIDE-seq* (Tsai et al. 2015): requires incorporation of a dsODN tagging oligonucleotide into cells, limiting its use to dividing cells. Sensitivity: approximately 0.1%.

*CIRCLE-seq* (Tsai et al. 2017): an in vitro cleavage assay on purified genomic DNA, highly sensitive but may overestimate risk by not accounting for chromatin structure.

*DISCOVER-seq* (Wienert et al. 2019): detects DSB repair factor (MRE11) accumulation at cut sites by ChIP-sequencing; requires no exogenous reagents and works in primary cells.

*Digenome-seq* (Kim et al. 2015): in vitro cleavage of purified genomic DNA followed by whole-genome sequencing.

Each method has distinct sensitivity, specificity, and applicability profiles. Regulatory agencies now typically expect at least two orthogonal methods for clinical-grade off-target evaluation of CRISPR therapies.

**What the clinical data actually show**

The off-target safety record of approved CRISPR therapies is, to date, reassuring but limited by follow-up duration and patient numbers.

For Casgevy, the BCL11A enhancer guide was selected from among candidates specifically to minimise off-target risk: the target sequence has unusually low homology to any other site in the human genome (fewer than 5 mismatches to non-target sites, concentrated in gene-poor regions). GUIDE-seq analysis in CD34+ cells found no detectable editing above the 0.1% sensitivity threshold at any of the ~30 high-priority predicted off-target sites. In the CLIMB trials, long-term follow-up (extending to 4+ years in some patients) has not revealed any clinical adverse events attributable to off-target editing — no evidence of clonal expansion suggesting oncogenic transformation, no hematological abnormalities inconsistent with the expected reconstitution of edited marrow. This is genuinely good news, but it should be read alongside several important caveats: the patient population is small (combined N < 100 with multi-year follow-up as of early 2026); the BCL11A enhancer guide was among the most carefully selected in the entire field; and the cancers most relevant to concern (leukemias arising from HSC clonal expansion) can have latencies of 5–20 years, which is beyond current follow-up.

For in vivo delivery platforms (NTLA-2001/nexiguran ziclumeran, CTX310), the safety profile is different in one important respect: the cells being edited cannot be removed, quality-checked, or recalled once the LNP infusion has been administered. The regulatory burden for demonstrating off-target safety is therefore higher, and the clinical safety data currently available are from small Phase 1 cohorts with follow-up of 1–2 years.

**The off-target argument and germline editing**

The scientific basis for the international consensus that germline editing "remains unacceptable at this time" rests in part on the off-target problem. In somatic editing, a small number of cells with off-target edits may be acceptable — they are bounded by the individual patient. In germline editing, every off-target event would be transmitted to all cells of the resulting person and to every subsequent generation. The He Jiankui experiment was, among other things, a clinical case study in off-target risk: his own sequencing data, selectively presented, failed to exclude off-target cleavage events in the edited embryos. The scientific community's reaction was not merely ethical revulsion — it was also genuine alarm that off-target safety in human embryos had not been, and given current tools cannot yet be, adequately characterised before the resulting person is born.

**What remains unknown**

Several important safety questions remain open. First, do any of the chromosomal rearrangements detectable in edited cell populations persist in vivo, and if so do they confer growth advantage over time? Second, are there cell-context-specific off-target sites that are not captured by GUIDE-seq in CD34+ cells used for Casgevy but would be relevant in other cell types? Third, does the transient RNA off-target activity of base editors have any phenotypic consequence in patient cells? Fourth — and most importantly from a public health standpoint — will the incidence of secondary malignancies in CRISPR-treated patients over the next decade differ from the background rate in patients treated by other means? These questions will only be answered by the long-term follow-up registries and post-marketing surveillance programs that regulatory agencies have required as conditions of Casgevy's approval.

## Questions to think about

1. GUIDE-seq detects off-target sites at approximately 0.1% clonal frequency. If 1 in 1,000 CD34+ stem cells has an off-target edit at a gene associated with clonal haematopoiesis (e.g., TET2, DNMT3A), is that clinically meaningful? What would a well-designed post-market surveillance study need to measure to answer this question, and over what timeframe?

2. The ex vivo setting of Casgevy allows each batch of edited cells to be tested for off-target editing before infusion — a safety check that in vivo LNP-delivery approaches cannot replicate. As in vivo delivery moves to new organs (liver, eye, heart), what safety governance framework should apply to ensure that off-target risk is adequately characterised before large Phase 3 trials enrol hundreds of patients?

3. Base editing avoids double-strand breaks, which reduces one class of off-target risk (chromosomal rearrangements), but introduces a new one (deaminase activity on non-targeted DNA/RNA). Is the net safety improvement over Cas9 unambiguous, or does the answer depend on the specific application and the specific base editor being used?
