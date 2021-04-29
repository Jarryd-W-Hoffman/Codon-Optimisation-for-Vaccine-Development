"""
codon_optimisation.py

Description:
This script optimises virus codons as part of an effort to create a vaccine. It manipulates the digital code
represented by nucleotides A, C, G, and U/T to enhance compatibility with a target vaccine. The optimisation process
is crucial for efficient protein expression, proper folding, and ultimately, the efficacy and safety of the vaccine
development process.

Author:
Jarryd Hoffman

Date:
12/04/2021
"""

# Program to optimise codons of a virus in an attempt to create a vaccine
import csv
import time

# Used to store a dictionary mapping codons to the amino acids they encode
codon_amino_acid_map = {}

def get_amino_acid(codon):
    """
    Returns the amino acid encoded by the given codon.

    Retrieves the amino acid information from the preloaded codon-aminoacid mapping.
    
    Note: Includes bugfix from Lucas Martins.

    Arguments:
        codon (str): The three-letter codon for which the amino acid is to be retrieved.

    Returns:
        str: The single-letter code representing the amino acid encoded by the given codon.
    """
    # Check if the codon-aminoacid mapping is empty
    if len(codon_amino_acid_map) <= 0:
        # Load codon-aminoacid mapping from the CSV file
        with open("codon-aminoacid.csv") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                codon_row = row["codon"]
                amino_acid = row["aminoacid"]
                codon_amino_acid_map[codon_row] = amino_acid

    # Retrieve the amino acid for the given codon from the mapping
    return codon_amino_acid_map[codon]

def read_codons(filename):
    """
    Reads codons from the specified file and returns them as a list in the order they appear.

    Arguments:
        filename (str): The name of the file containing codons.

    Returns:
        list: A list of codons read from the file.
    """
    codons = []
    with open(filename) as input_file:
        #  Read in three characters at a time, since each codon is three characters
        data = input_file.read(3)
        while data.strip() != "":
            codons.append(data)
            data = input_file.read(3)
    return codons

def compare(attempt, target):
    """
    Compares two lists of codons and calculates the percentage of identical codons.

    Arguments:
        attempt (list): A list of codons to be compared with the target.
        target (list): A list of codons to be compared to.

    Returns:
        float: The percentage of codons that are identical between the attempt and the target.
    """
    count = 0
    for i in range(len(target)):
        if attempt[i] == target[i]:
            count += 1
    return 100 * count / len(target)

def optimise_codons(codons):
    """
    Optimises the given codons using the method specified in readme.md.

    Arguments:
        codons (list): A list of codons to optimise.

    Returns:
        list: An optimised list of codons.
    """
    optimised = []

    for codon in codons:
        # Method to check and replace third character of codon
        if codon[2] in "GC":
            # No change required - Third char already equals desired output
            # print("No change required - Codon: " + codon + " already " +
            # "equals the desired output")
            pass
        else:
            # Copy original codon
            properties = codon
            # Apply 'C' to the third character of codon
            codon = codon[:2] + "C"
            # print("Codon modified (M/O): " + codon + "/" + properties)
            # Check if new codon amino acid matches original
            if (get_amino_acid(codon) == get_amino_acid(properties)):
                # print("Modified codon (" + get_amino_acid(codon) + ") " +
                # "matches original codon (" + get_amino_acid(properties) + ")")
                pass
            else:
                # Copy original codon
                properties = codon
                # Apply 'G' to the third character of codon
                codon = codon[:2] + "G"
                # print("Codon modified (M/O): " + codon + "/" + properties)

        # Method to remap codons to make use of possible start
        # codons and stop codons
        if get_amino_acid(codon) == "L":
            if codon[2] in "G":
                # No change required - Third char already equals desired output
                pass
            else:
                # Copy original codon
                properties = codon
                # Remap 'ATC' to 'G' for third character of codon
                codon = codon[:2] + "G"  # Preferred output
                # print("Codon modified (M/O): " + codon + "/" + properties)

        if get_amino_acid(codon) == "M":
            # No change required - Third char already equals desired output
            # (Only 1 codon in amino acid group)
            pass  # Possible start codon

        if get_amino_acid(codon) == "V":
            if codon[2] in "G":
                # No change required - Third char already equals desired output
                pass
            else:
                # Copy original codon
                properties = codon
                # Remap 'ACT' to 'G' for third character of codon
                codon = codon[:2] + "G"  # Possible start codon
                # print("Codon modified (M/O): " + codon + "/" + properties)
        
        if get_amino_acid(codon) == "s":
            if codon[2] in "A":
                pass
            else:
                # Copy original codon
                properties = codon
                # Remap 'A' to 'G' for second character of codon
                codon = codon[0] + "G" + codon[2]  # stop codon
                # print("Codon modified (M/O): " + codon + "/" + properties)

        optimised.append(codon)

    return optimised

if __name__ == "__main__":
    """
    Read in the virus and vaccine codons, perform optimisation, and compare the results.

    This block measures the time taken for the codon optimisation process, compares the optimised
    codons with the original virus and the target vaccine, and outputs the statistics and results
    of the optimisation process.
    """
    #  Read in virus
    virus = read_codons("virus.txt")
    #  Read in vaccine
    vaccine = read_codons("vaccine.txt")

    # Measure the time taken for optimisation
    start_time = time.time()

    #  Optimise
    optimised = optimise_codons(virus)

    # Calculate the time taken for optimisation
    optimisation_time = time.time() - start_time

    #  Compare virus and optimised version to vaccine
    virus_comparison = compare(virus, vaccine)
    optimised_comparison = compare(optimised, vaccine)

    # Output results, including improvement from optimisation
    print("--------------------------------------------")
    print("Codon Optimisation Results:")
    print("--------------------------------------------")
    print("- Original Virus Codons:", " ".join(virus[:10]), "...")
    print("- Optimised Codons:", " ".join(optimised[:10]), "...")
    print("- Target Vaccine Codons:", " ".join(vaccine[:10]), "...")
    print("\n--------------------------------------------")
    print("Optimisation Statistics:")
    print("--------------------------------------------")
    print("- Percentage of Identical Codons:")
    print(f"  - Original vs. Optimised: {virus_comparison:.2f}%")
    print(f"  - Optimised vs. Target Vaccine: {optimised_comparison:.2f}%")
    print(f"  - Optimisation compatibility: {optimised_comparison - virus_comparison:.2f}%")
    print("\n- Total Codons:", len(virus))
    print(f"- Optimisation Time: {optimisation_time:.2f} seconds")
