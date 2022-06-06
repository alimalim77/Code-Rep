// { Driver Code Starts
#include <stdio.h>

int largest(int arr[], int n);

int main() {
    int arr[1000];
    int i, t, n;
    scanf("%d", &t);
    while (t--) {
        scanf("%d", &n);
        for (i = 0; i < n; i++) scanf("%d", &arr[i]);
        printf("%d", largest(arr, n));
        printf("\n");
    }
    return 0;
}
// } Driver Code Ends


// C function to find maximum in arr[] of size n
int largest(int arr[], int n) {
    int num = 0, i=0;
    for(i=0; i < n; i++){
        if (num<arr[i])
        num = arr[i];
    }
    return num;
}