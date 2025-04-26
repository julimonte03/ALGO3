#include <iostream>
#include <vector>
using namespace std;

int mirrorIndex(vector<int>& nums) {
    int low = 0, high = nums.size() - 1;

    while (low <= high) {
        int mid = low + (high - low) / 2;

        if (nums[mid] == mid) {
            return mid;
        } else if (nums[mid] > mid) {
            high = mid - 1;
        } else {
            low = mid + 1;
        }
    }

    return -1; 
}

int main() {
    // Casos de prueba

    // Caso 1: Índice espejado en el medio
    vector<int> arr1 = {-4, -1, 2, 4, 7};
    cout << "Resultado caso 1: " << mirrorIndex(arr1) << endl;  // Debería retornar 2

    // Caso 2: Índice espejado en el extremo izquierdo
    vector<int> arr2 = {0, 2, 3, 4, 5};
    cout << "Resultado caso 2: " << mirrorIndex(arr2) << endl;  // Debería retornar 0

    // Caso 3: No hay índice espejado
    vector<int> arr3 = {-3, -1, 1, 5, 6};
    cout << "Resultado caso 3: " << mirrorIndex(arr3) << endl;  // Debería retornar -1

    // Caso 4: Índice espejado en el extremo derecho
    vector<int> arr4 = {-5, -4, -3, -1, 4};
    cout << "Resultado caso 4: " << mirrorIndex(arr4) << endl;  // Debería retornar 4

    // Caso 5: Lista vacía
    vector<int> arr5 = {};
    cout << "Resultado caso 5: " << mirrorIndex(arr5) << endl;  // Debería retornar -1

    return 0;
}
