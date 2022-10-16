
def fun_gc_bounds(gc_bounds, GC_content):
    left_border = 0.0
    rigth_border = 100.0
    if isinstance(gc_bounds, float) | isinstance(gc_bounds, int) == True:
        rigth_border = float(gc_bounds)
    else:
        left_border = float(gc_bounds[0])
        rigth_border = float(gc_bounds[1])
    if left_border < GC_content < rigth_border:
        return(True)
    else:
        return(False)


def fun_length_bounds(length_bounds, counter):
    left_border = 0.0
    rigth_border = float(2**32)
    if isinstance(length_bounds, float) | isinstance(length_bounds, int) == True:
        rigth_border = float(length_bounds)
    else:
        left_border = float(length_bounds[0])
        rigth_border = float(length_bounds[1])
    if left_border < counter < rigth_border:
        return(True)
    else:
        return(False)


def fun_qual_thresh(qual_strok, quality_threshold = 0.0):
    qual = 0
    cou = 0
    for k in qual_strok:
        qual += ord(k)
        cou += 1
    if (qual/cou) < quality_threshold:
        return(False)
    else:
        return(True)



passed = "_passed.fastq"


def main(input_fastq, output_file_prefix, gc_bounds = (0, 100), length_bounds = (0, 2**32), quality_threshold = 0, save_filtered = False):
    with open(input_fastq, "r") as file, open(f"{output_file_prefix}{passed}", "w") as ouf:
        spis = []
        for line in file:
            spis += [line.strip()]
        indicess = []
        index_fail = []
        for i in range(len(spis)):
            if (i - 1) % 4 == 0:
                counter = 0
                GC = 0
                AT = 0
                for j in spis[i]:
                    counter += 1
                    if j == "G":
                        GC += 1
                    elif j == "C":
                        GC += 1
                    elif j == "A":
                        AT += 1
                    elif j == "T":
                        AT += 1
                GC_content = GC / (GC + AT) * 100
                GC_cont = fun_gc_bounds(gc_bounds, GC_content)
                length_OK = fun_length_bounds(length_bounds, counter)
                if GC_cont == True and length_OK == True:
                    indicess += [i]
                else:
                    index_fail += [i]
        indices_passed = []
        for i in indicess:
            passed_read = fun_qual_thresh(qual_strok=spis[i + 2], quality_threshold=float(quality_threshold))
            if passed_read == True:
                indices_passed += [i]
            else:
                index_fail += [i]
        for i in indices_passed:
            ouf.write(f"{spis[i - 1]}\n")
            ouf.write(f"{spis[i]}\n")
            ouf.write(f"{spis[i + 1]}\n")
            ouf.write(f"{spis[i + 2]}\n")
        if save_filtered == True:
            failed = "_failed.fastq"
            output_file_name = f"{output_file_prefix}{failed}"
            with open(output_file_name, 'w') as failed_reads:
                for i in index_fail:
                    failed_reads.write(f"{spis[i - 1]}\n")
                    failed_reads.write(f"{spis[i]}\n")
                    failed_reads.write(f"{spis[i + 1]}\n")
                    failed_reads.write(f"{spis[i + 2]}\n")

