#include <stdio.h>
#include <stdlib.h>

typedef unsigned long long int lint;

const lint powerOfTen[] = {
    10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000, 10000000000, 100000000000, 1000000000000, 10000000000000, 100000000000000, 1000000000000000, 10000000000000000, 100000000000000000
};

lint nDigits (lint n) {
    lint r = 1;
    while (n > 9) {
        n /= 10;
        r++;
    }
    return r;
}

lint *blink(lint *arr, lint *len){
    lint *data = malloc(sizeof(lint) * *len * 2);
    if(data == NULL) {exit(1);}

    lint nOfDigits;

    lint _l = *len;
    lint offset = 0;
    for (size_t i = 0; i < _l; i++){
        if(arr[i] == 0){
            data[i+offset] = 1;
        }else if((nOfDigits = nDigits(arr[i])) % 2 == 0){
            data[i+offset] = arr[i] / powerOfTen[nOfDigits/2-1];
            offset += 1;
            data[i+offset] = arr[i] % powerOfTen[nOfDigits/2-1];
        }else{
            data[i+offset] = arr[i] * 2024;
        }
    }
    *len += offset;
    free(arr);
    return data;
}

void printData(lint arr[], lint len){
    printf("[");
    for(size_t i = 0; i < len; i++){
        printf("%d, ", arr[i]);
    }
    printf("] of %d elements\n", len);
}

int main(void){
    lint len = 8;
    lint *data = malloc(sizeof(lint) * len);
    data[0] = 7725;
    data[1] = 185;
    data[2] = 2;
    data[3] = 132869;
    data[4] = 0;
    data[5] = 1840437;
    data[6] = 62;
    data[7] = 26310;

    for(size_t i = 0; i < 75; i++){
        data = blink(data, &len);
        printf("(%d / 75)\n", i + 1);
        // printData(data, len);
    }

    printf("%d\n", len);
    free(data);
}