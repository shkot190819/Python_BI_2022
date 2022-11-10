import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter, AutoMinorLocator)

def read_gff(gff_annotation_file_name):
    gff_annotation = pd.read_csv(gff_annotation_file_name, sep='\t', skiprows=1, header=None, names=['seq_id', 'source', 'type', 'start', 'end', 'score', 'strand', 'phase', 'attributes'])
    return gff_annotation
read_gff('rrna_annotation.gff')


def read_bed6(name_of_bed_file):
    bed_file = pd.read_csv(name_of_bed_file, sep='\t', header=None, names=['chrom','chromStart','chromEnd','name','score','strand'])
    return bed_file
read_bed6('alignment.bed')


df = read_gff('rrna_annotation.gff')
df['attributes'] = df.attributes.str.extract(r'=(\d+S)', expand=True)

RNA_type_data = df.groupby(['seq_id','attributes'])
RNA_type_data = RNA_type_data['attributes'].count().to_frame(name = 'count').reset_index().rename(columns={"attributes": "RNA_type", "seq_id": "sequence"})
RNA_type_data


data_for_plotting = pd.pivot(RNA_type_data, values='count', index=['sequence'], columns=['RNA_type'])
data_for_plotting.plot(kind="bar")
plt.xlabel('Sequence', fontsize=18, fontweight='bold')
plt.ylabel('Count', fontsize=16, fontweight='bold')


diffexpr_data = pd.read_csv('diffexpr_data.tsv.gz', sep='\t')
diffexpr_data['quality'] = np.where((diffexpr_data['log_pval']>-np.log10(0.05)) & (diffexpr_data['logFC']>=0), "Significantly upregulated",
                                    np.where((diffexpr_data['log_pval']>-np.log10(0.05)) & (diffexpr_data['logFC']<0), "Significantly downregulated",
                                             np.where((diffexpr_data['log_pval']<=-np.log10(0.05)) & (diffexpr_data['logFC']<0), "Non-significantly downregulated",
                                                      np.where((diffexpr_data['log_pval']<=-np.log10(0.05)) & (diffexpr_data['logFC']>=0), "Non-significantly upregulated", np.nan))))
diffexpr_data


plt.rcParams["figure.figsize"] = (16,10)
plt.rcParams['font.weight'] = 'bold'
fig, ax = plt.subplots()
palette ={"Significantly downregulated": "C0", "Significantly upregulated": "C1", "Non-significantly downregulated": "C2", "Non-significantly upregulated": "C3"}
sns.scatterplot(x="logFC", y="log_pval", hue='quality', data=diffexpr_data, palette=palette, linewidth = 0, s=20)

plt.rcParams['xtick.labelsize'] = 16
plt.rcParams['ytick.labelsize'] = 16

min_value = float(np.min(diffexpr_data[['logFC']]))
max_value = float(np.max(diffexpr_data[['logFC']]))
boundary = max([np.sqrt(min_value**2), np.sqrt(max_value**2)])+1

ax.set_xlim(-boundary, boundary)
lgnd = ax.legend(fontsize = 16, framealpha=1, shadow=True, borderpad=1)
for handle in lgnd.legendHandles:
    handle.set_sizes([200])

plt.axhline(y=-np.log10(0.05), color='#5d5d5d', linestyle='dashed', label='p value = 0.05')
plt.axvline(0, color='#5d5d5d', linestyle='dashed')
plt.text(8, 2.5, 'p value = 0.05', ha='left', va='center', fontsize=16, color='#5d5d5d')
plt.title('Volcano plot', fontweight='bold', style='italic', fontsize=30)
plt.xlabel(r'$\bf{log_2(fold\ change)}$', fontsize=18)
plt.ylabel(r'$\bf{-log_{10}(p\  value\  corrected)}$', fontsize=18)

ax.xaxis.set_major_locator(MultipleLocator(5))
ax.xaxis.set_major_formatter(FormatStrFormatter('%d'))
ax.xaxis.set_minor_locator(MultipleLocator(1))

ax.yaxis.set_major_locator(MultipleLocator(20))
ax.yaxis.set_major_formatter(FormatStrFormatter('%d'))
ax.yaxis.set_minor_locator(MultipleLocator(5))

ax.xaxis.set_tick_params(reset=True, width=2, size=10, colors='black', color='black', top=False)
ax.xaxis.set_tick_params(reset=True, which='minor', width=2, size=5, colors='black', color='black', top=False)
ax.yaxis.set_tick_params(reset=True, width=2, size=10, colors='black', color='black', top=False)
ax.yaxis.set_tick_params(reset=True, which='minor', width=2, size=5, colors='black', color='black', top=False)

plt.rcParams['xtick.minor.width'] = 2
plt.rcParams['xtick.minor.size'] = 5
plt.rcParams['ytick.minor.width'] = 2
plt.rcParams['ytick.minor.size'] = 5

for axis in ['top','bottom','left','right']:
    ax.spines[axis].set_linewidth(2)
    ax.spines[axis].set_color('black')

plt.arrow(x=-9.2, y=10, dx=0, dy=-5, width=.08, facecolor='red', edgecolor='black', head_length=1.5)
plt.annotate('MUC7', xy = (-9.5,12))

plt.arrow(x=-10.5, y=60, dx=-0.1, dy=-5, width=.08, facecolor='red', edgecolor='black', head_length=1.5)
plt.annotate('UMOD', xy = (-10.9,62))

plt.arrow(x=4.2, y=12, dx=.05, dy=-5, width=.08, facecolor='red', edgecolor='black', head_length=1.5)
plt.annotate('ZIC5', xy = (3.8,14.2))

plt.arrow(x=4.5, y=11, dx=.05, dy=-5, width=.08, facecolor='red', edgecolor='black', head_length=1.5)
plt.annotate('ZIC2', xy = (4.3,12.5))

plt.savefig("volcano_plot.png", bbox_inches="tight", dpi=300)
plt.show()