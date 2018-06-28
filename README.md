# bpsomatic
Bioinformatic pipeline for calling somatic variants from NGS-data. This pipeline is in progress and will be improved regularly. The aim is to make a simple to use pipeline that can produce high-quality variant calls.

This pipeline is based on Broad Institute's Genome Analysis Toolkit (GATK). https://software.broadinstitute.org/gatk/
The name 'bpsomatic' is derived from GATK's "Best practices" workflow so that it would be "Best Practices Somatic". (GATK Best practices for somatic variant calling https://software.broadinstitute.org/gatk/best-practices/workflow?id=11146) 

The best practices workflow ensures that the GATK tools perform optimal analysis on the given data. I'll make sure that this pipeline itself uses only GATK best practices to get the best possible results for users. So if you spot something that is not a GATK best practice, let me know!
(NOTE At the moment this pipeline does not preprocess data (alignment etc.) so it is up to the user to make sure that the best practices have been applied during these steps! Also if user doesn't provide Panel of normals for the analysis it technically isn't GATK best practice.)
