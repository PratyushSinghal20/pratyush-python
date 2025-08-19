#include <stdio.h>

int main(){
    int y,m,w;
    int days;
    printf("enter days");
    scanf("%d",&days);
    y=days/365;
    if(y>=1){
        days=days-(y*365);
        m=days/30;
        if(m>=1){
            days=days-(m*30);
            w=days/7;
            if(w>=1){
                days=days-(w*7);
            }
        }
        
    }
    else if(y<1){
        m=days/30;
         if(m>=1){
            days=days-(m*30);
            w=days/7;
            if(w>=1){
                days=days-(w*7);
            }
        else{
            w=days/7;
            if(w>=1){
                days=days-(w*7);
            }


        }
    }
        


     
    printf("%d years %d month %d weeks %d days are there",y,m,w,days);
    return 0;
    }
}
