args <- commandArgs(trailingOnly=TRUE)

A_data = scan(file="A_distribution.txt", what='integer')
B_data = scan(file="B_distribution.txt", what='integer')
#print(b)
Mode <- function(x) {
    ux <- unique(x)
    ux[which.max(tabulate(match(x, ux)))]
}


Median <- function(x){

	median(as.numeric(args[x]))
}
#median(as.numeric(args))


Standard_Deviation <- function(x){
	sd(x)
}


print(median(as.numeric(A_data)))
print(sd(as.numeric(A_data)))
print(Mode(as.numeric(A_data)))
hist(as.numeric(A_data))


print(median(as.numeric(B_data)))
print(sd(as.numeric(B_data)))
print(Mode(as.numeric(B_data)))
hist(as.numeric(B_data))
# if (tolower(args[1]) == "median") {
# 	Median(as.numeric(args[2]))
# }else if (tolower(args[1]) == "mode"){
# 	Mode(as.numeric(args[2]))
# }else if (tolower(args[1]) == "standard_deviation"){
#  	Standard_Deviation(as.numeric(args[2]))
# }else 
#  	print("Command not found")