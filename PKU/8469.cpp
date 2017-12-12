//8469

#include <iostream>
#include <cstdio>
#include <string>

n = 30;
char[30] current;
char[30] target;

void setBit(char &c, int i, int v){

}

int getBit(char c, int i){

}


int main(){
  cin >> current;
  cin >> target;
  N = strlen(current);
  bool to_change = false;
  // Don't toggle 1st
  int i = 0
  //for(int i = 0; i < N; i++){
  while(i < N){
    if (to_change){
      current[i] = ~current[i];
      to_change = false;
    }
    if (current[i] != target[i]){
      to_change = true;
      i++;
    }
  }

  // Toggle first

}
