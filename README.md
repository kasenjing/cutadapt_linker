# cutadapt_linker
Modified cutadapt to make it capable of trim linker and separate reads alongside the linker to different output file.

------
The purpose of this modification is that ChIA-PET Utility's incapable of processing linker longer than 32 base pair and cutadapt always trims the sequences on one side of adapter. The modification makes cutadapt finds an adapter (linker) in read 1 and/or read 2 and write both sequence on side of adapter to output read 1 and output read 2 while retaining other filter function of cutadapt (not tested).

## Requirement
```
    python >= 3.8
    gcc
    setuptools_scm
```
## Installation
```
    git clone https://github.com/kasenjing/cutadapt_linker.git
    cd cutadapt_linker
    python setup.py bdist_egg
    python setup.py install
```

## Usage

```
    cutadapt2 -o linker_left.fq.gz -p linker_right.fq.gz --linker -b ACGCGATATCTTATTGACT -O 6 --discard-untrimmed -j 4 -e 2 -m 18 r1_input.fq.gz r2_input.fq.gz
```

Parameter
|Para|Description|
|---|---|
|-o|Sequence on the left of linker|
|-p|Sequence on the right of linker|
|--linker|Tell cutadapt to find linker instead of trim adapter|
|-b|linker sequence|
|-O|Minimal overlap for sequence to be considered as partial linker|
|--discard-untrimmed|Retain reads with linker|
|-j|Threads|
|-e|Error base in linker for sequencing error|
|-m|Minimal read length to write to output|

## Description
![image](doc/example.jpg)