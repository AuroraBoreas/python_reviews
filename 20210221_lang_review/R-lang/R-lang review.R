# var

x <- 3;
y <- 2.718;
a <- "hello";
b <- "world";

# data types
# [x] C
# [x] S
# [*] I
# [*] L
# [*] F
# [*] D
# [x] B
# [*] B
# [x] D
# [*] S

# type traits

# type conversion

# operators
# [*] A
# [*] R
# [*] L
# [*] A
# [] B
# [*] A
# [] C
# [] O
# [] O

# functions
func_name <- function(arg1, arg2, arg3){
    return (arg1 + arg2 + arg3);
}

# containers
# vector
x <- c(1, 2, 3);

# factor
y <- factor(c("mon", "fri", "sat", "sun", "tue", "wed", "thu", "fri"), 
            level=c("mon, tue, wed, thu, fri, sat, sun"));

# list
z <- list(1, 2, 3);

# matrix
outMatrix <- matrix(c(...), 
                    nrow = nrow, 
                    ncol = ncol, 
                    byrow = byrow);

# statement, expression
x1 <- 6 * 10 / 6 * 10;
x2 <- (3 + 4) * (4 - 5);

# control flow
# if...else if...else
# try...catch...finally

# loop
# for(;;) { ...; }
# while(condi) { ...; }
# repeat{ ...; }
# keywords: continue, break
a1 <- c(1, 2, 3, 4);
for(i=0;i<3;++i)
{
    print(a1[i]);
}

i = 0;
while(TRUE)
{
    print(a1[i]);
    i = i + 1;
    if(i==3) { break; }
}

i = 0;
repeat
{
    print(a1[i]);
    i = i + 1;
    if(i==3) { break; }
}

# install packages
install.packages("tidyverse");

# include packages
library("tidyverse");

# "tidy data"
# 1, every variable has its own column;
# 2, every observation has it own row;
# 3, every value has its own cell;

# howto: "gather, combine, split,"

# gglot()
# geom_point()
# geom_violin()
# geom_bar()
# geom_col()
# geom_line()
# geom_scatter()
# scale_x_continue()
# scale_y_continue()