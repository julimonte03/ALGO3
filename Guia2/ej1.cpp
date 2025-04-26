#include <iostream>
#include <vector>
using namespace std;

bool dominLeft(vector<int> nums){
    
    int top = nums.size();
    int mid = nums.size()/2; 

    while (top > 1){

        int leftSum = 0, rightSum = 0;

        for(int i = 0; i < mid; i++){

            leftSum += nums[i];
        }
        
        for(int i = mid; i < top; i++){

            rightSum += nums[i];
        }

        if(leftSum <= rightSum) return false; 

        top = mid;  
        mid = top /2;

    }
    
    return true;

}

int main(){

    // Ejemplo de uso con un arreglo que es "más a la izquierda"
    vector<int> arr1 = {8, 6, 7, 4, 5, 1, 3, 2};
    
    // Ejemplo de uso con un arreglo que NO es "más a la izquierda"
    vector<int> arr2 = {8, 4, 7, 6, 5, 1, 3, 2};
    
    if (dominLeft(arr1)) {
        cout << "El arreglo {8, 6, 7, 4, 5, 1, 3, 2} es más a la izquierda." << endl;
    } else {
        cout << "El arreglo {8, 6, 7, 4, 5, 1, 3, 2} NO es más a la izquierda." << endl;
    }
    
    if (dominLeft(arr2)) {
        cout << "El arreglo {8, 4, 7, 6, 5, 1, 3, 2} es más a la izquierda." << endl;
    } else {
        cout << "El arreglo {8, 4, 7, 6, 5, 1, 3, 2} NO es más a la izquierda." << endl;
    }

    return 0;
}