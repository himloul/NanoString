library(nanostringr)
library("gplots")
library("RColorBrewer")
library("NanoStringQCPro")

#### DATA PREP ####

# reacc<-read_rcc("csdata")
# 
# a<-parse_counts("csdata/GSM2055832_10_4050_PD_mRNA.RCC")
# a<-as.data.frame(a)
# unique(a$Code.Class)
# # a<-subset(a,select=-c(Name,Accession))
# 
# # Normalization
# a <- HKnorm(a, is.logged = FALSE, corr = 1e-04)
# # Rename rows by Name
# rownames(a) <- a$Name
# # Subset the dataset
# a<-subset(a,select=-c(Name,Accession))

# ----------------------------------------------
#### 3.1.2 ####

reacc<-read_rcc("csdata")
reacc

b = as.data.frame(reacc$exp)

a <- reacc$raw
a<-as.data.frame(a)
dt = a[a$Code.Class == "Negative" | a$Code.Class == "Positive",]

# Rename rows by Name
rownames(dt) <- dt$Name

# Subset the dataset
dt <- subset(dt,select=-c(Name,Accession, Code.Class))

# Create the matrix input
input = as.matrix(dt)

# Colors
condition_colors <- rainbow(ncol(input), start = 0, end = .3)

# The heatmap
heatmap(input, col=bluered(20), cexRow=1, cexCol=1, margins = c(20,13), ColSideColors=condition_colors, scale="row")

# -------------------------------------
#### 3.2.2 ####

# Quality Control
mcl1.r = a[a$Name == "MCL1" | a$Name == "CXCL1" | a$Code.Class == "Housekeeping" | a$Code.Class == "Positive" | a$Code.Class == "Negative",]
NanoStringQC(raw = a, exp = b)

# Prepare data before data analysis
baseline = c("GSM2055824_02_4355_PD_mRNA", "GSM2055826_04_4078_PD_mRNA", "GSM2055828_06_3746_PD_mRNA", "GSM2055830_08_3790_PD_mRNA", "GSM2055832_10_4050_PD_mRNA")
posttraitement = c("GSM2055823_01_4353_PD_mRNA", "GSM2055825_03_3366_PD_mRNA", "GSM2055827_05_4846_PD_mRNA", "GSM2055829_07_3760_PD_mRNA", "GSM2055831_09_4436_PD_mRNA")

# data manipulation: transform columns indicating file's names to row values.
library(reshape2)
data = a[a$Name == "MCL1" | a$Name == "CXCL1",]
data = melt(data = data, id=c("Code.Class","Name", "Accession"))
# Add column : Timepoint
data = transform(data, Timepoint = ifelse(is.element(variable,baseline) == 1, "Baseline", "Post traitement"))

# BOXPLOT
boxplot(value~Timepoint*Name,data=data, main="Boxplots", xlab="TimePoint", ylab="Value")

# SUMMARY
tapply(data$value, data$Name, summary)


