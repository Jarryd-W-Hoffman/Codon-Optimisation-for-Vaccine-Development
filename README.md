# Codon Optimisation for Vaccine Development
## Introduction
This project aims to optimise codons of a virus as part of an effort to create a vaccine. The optimisation process involves manipulating the DNA's digital code, represented by nucleotides A, C, G, and U/T. In nature, these nucleotides are molecules stored as chains in DNA or RNA. The optimisation process is crucial for enhancing compatibility with a target vaccine.

## DNA as a Digital Code
### Nature's Code
DNA serves as a digital code in nature, with A, C, G, and U/T representing the building blocks of life. Unlike computer systems that use 0 and 1, nature utilises these nucleotides to store information in the form of codons. A codon, consisting of three nucleotides, is the basic unit of processing in biological systems.

### Computer Analogies
Drawing a parallel to computer systems, where 0 and 1 are stored as various physical manifestations, the digital code in DNA is embodied by molecules. Just as computers group 8 bits into a byte, nature groups 3 nucleotides into a codon. Each codon contains 6 bits of information, allowing for 64 different codon values.

### Mathematical Perspective
Mathematically, the arrangement of nucleotides in a codon can be understood as follows:
- Each nucleotide (A, C, G, or U/T) is represented by 2 bits.
- Since a codon consists of 3 nucleotides, it contains a total of 6 bits (2 bits * 3 nucleotides).
- This implies that there are 2⁶ (2 to the power of 6) or 64 different possible codon values.

## RNA Strain and COVID-19
In this project, we focus on the RNA strain of the BioNTech/Pfizer vaccine, which is designed to combat COVID-19. The RNA-based vaccines leverage the genetic information encoded in RNA to stimulate an immune response in the body, aiding in the development of immunity against the virus.

### mRNA Vaccines and the BNT162b2 mRNA Vaccine
The BNT162b2 mRNA vaccine is at the core of this project. It consists of a digital code that is 4284 characters long, roughly fitting within the constraints of a series of tweets. At the onset of the vaccine production process, this digital code was uploaded to a DNA printer. The DNA printer converted the bytes on disk into actual DNA molecules.

#### Vaccine Production Process
Tiny amounts of DNA are produced from the DNA printer, and after extensive biological and chemical processing, they transform into RNA, which eventually ends up in the vaccine vial. A 30 microgram dose of the vaccine genuinely contains 30 micrograms of RNA. Additionally, a clever lipid (fatty) packaging system facilitates the delivery of mRNA into our cells.

##### Resources for Further Reading
- Derek Lowe's comprehensive post [“RNA Vaccines And Their Lipids”](https://www.science.org/content/blog-post/rna-vaccines-and-their-lipids) explains the lipid and delivery aspects of the vaccines in detail.

- [Jonas Neubert and Cornelia Scheitz](https://blog.jonasneubert.com/2021/01/10/exploring-the-supply-chain-of-the-pfizer-biontech-and-moderna-covid-19-vaccines/) have written an informative page with details on how the vaccines are produced and distributed.

- Bert Hubert's article [Reverse Engineering the source code of the BioNTech/Pfizer SARS-CoV-2 Vaccine](https://berthub.eu/articles/posts/reverse-engineering-source-code-of-the-biontech-pfizer-vaccine/) provides insights into the reverse engineering of the source code of the BioNTech/Pfizer SARS-CoV-2 vaccine.

### RNA - Biology's 'Working Memory'
RNA is the volatile 'working memory' version of DNA. While DNA serves as the durable, internally redundant, and reliable storage in biology (similar to flash drive storage in computers), RNA acts as the temporary working memory. Much like computers do not execute code directly from a flash drive, biological systems copy genetic code to a faster, more versatile yet fragile system, which is RNA.

For computers, this is RAM; for biology, it is RNA. However, RNA degrades quickly unless carefully maintained. The fragility of RNA is why the Pfizer/BioNTech mRNA vaccine must be stored in extremely cold conditions, resembling the need to preserve RAM in computers.

#### RNA Size and Information Content
Each RNA character weighs on the order of 0.53·10⁻²¹ grams, meaning there are around 6·10¹⁶ characters in a single 30 microgram vaccine dose.

- In grams: 0.00003
- Weight per nucleotide: 5.30E-22
- Total nucleotides: 5.66E+16
- Bits per nucleotide: 2
- Bits per byte: 8
- Total data: 1.42E+16
- In TB: 1.42E+04
- In PB: 14.15
- Repetitions: 1.32E+13
- In billions: 13,212.83

Expressed in bytes, this is around 14 petabytes, although it must be said this consists of around 13,000 billion repetitions of the same 4284 characters. The repetition is a characteristic of the vaccine's digital code, where the same 4284-character sequence is intentionally repeated around 13,000 billion times. The actual informational content of the vaccine is just over a kilobyte. SARS-CoV-2 itself weighs in at around 7.5 kilobytes.

## Biological Significance of Codon Optimisation
Optimising codons in the context of vaccine development holds substantial biological significance. Codons, the three-nucleotide sequences that encode specific amino acids, play a pivotal role in the translation of genetic information into proteins. Here are key aspects highlighting the biological significance of codon optimisation:

- **Impact on Protein Expression and Folding:**
  - The choice of codons can influence the efficiency of protein expression. Strategic codon optimisation enhances the translation process, leading to increased production of the target viral proteins.
  - Certain codon biases in the natural genetic code may impact protein folding and stability. Codon optimisation seeks to mitigate these effects, ensuring the correct folding and functionality of the synthesised proteins.

- **Adaptation to Host Organism:**
  - Codon optimisation considers the host organism in which the vaccine will be produced. Different organisms have varying preferences for codon usage. Optimising codons according to the host organism's codon bias can improve the efficiency of translation and overall vaccine yield.

- **Enhanced Immune Response:**
  - The efficiency of protein expression directly influences the immune response triggered by a vaccine. Well-optimised codons contribute to the production of viral antigens in sufficient quantities, promoting a robust immune response. This is critical for the successful development of immunity against the target virus.

- **Safety and Consistency:**
  - Codon optimisation plays a role in ensuring the safety and consistency of vaccine production. By carefully selecting codons, we can minimise potential side effects or unintended consequences associated with the expression of viral proteins. Consistency in codon usage across batches is crucial for maintaining the uniformity and effectiveness of the vaccine.

Codon optimisation is not merely a computational process; it has profound implications for the biological outcomes of vaccine development. Strategic codon selection contributes to efficient protein expression, proper protein folding, and ultimately, the efficacy and safety of the developed vaccine.

## Repository Overview
### Files
- `codon_optimisation.py`: The main Python script for optimising virus codons based on specific rules.
- `virus.txt`: File containing the original virus codons.
- `vaccine.txt`: File containing the codons of the target vaccine.
- `codon-aminoacid.csv`: CSV file mapping each of the 64 possible codons to their respective amino acids.

### Functions
- `get_amino_acid(codon)`: Retrieves the amino acid encoded by a given codon.
- `read_codons(filename)`: Reads codons from a file and returns them as a list.
- `compare(attempt, target)`: Compares two lists of codons and returns the percentage of identical codons.
- `optimise_codons(codons)`: Optimiaes a list of codons based on specified rules.

## Usage
1. Clone the repository: `git clone https://github.com/Jarryd-W-Hoffman/Codon-Optimisation-for-Vaccine-Development.git`
2. Navigate to the project directory: `cd Codon-Optimisation-for-Vaccine-Development`
3. Run the optimisation script: `python codon_optimisation.py`

## Results
After running the `codon_optimisation.py` script, users can expect an output that provides insights into the optimisation process and the resulting codon sequences. 

Below is an example output:

```plaintext
--------------------------------------------
Codon Optimisation Results:
--------------------------------------------
- Original Virus Codons: ATG CTA GCG TCG ...
- Optimised Codons: ATG CTA ACG TCG ...
- Target Vaccine Codons: ATG CTA ACG TCG ...

--------------------------------------------
Optimisation Statistics:
--------------------------------------------
- Percentage of Identical Codons:
  - Original vs. Optimised: 85.2%
  - Optimised vs. Target Vaccine: 92.7%
  - Original vs. Target Vaccine: 80.1%

- Total Codons: 1024
- Optimisation Time: 0.35 seconds
```

The codon optimisation process successfully enhanced compatibility between the original virus codons and the target vaccine. The optimised codons demonstrate a higher similarity to the target vaccine, ensuring improved translation efficiency and potential efficacy in the vaccine development process.

Feel free to analyse the detailed results and explore the optimised codons to gain further insights into the impact of the optimisation rules on the genetic code.

## Codon-Aminoacid Mapping
The `codon-aminoacid.csv` file contains a mapping of each of the 64 possible codons to their respective amino acids. This mapping is essential for determining the amino acid encoded by a given codon during the optimisation process.
