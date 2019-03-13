//2.5.2019 - Shashi
//Program that accepts an integer array vector and returns : Count of positive numbers and Sum of negative numbers
//We use Vectors for this solution to help create more flexible, dynamic arrays.

using namespace std;
#include <vector> 
#include <iostream> 

//Function starts here
std::vector<int> countPositivesSumNegatives(std::vector<int> input)
{
    int countPositive=0; //positive counter
    int sumNegative=0;   //sum of negative values
    if(input.size()==0) return {}; //if input is empty, return blank
    //else loop through input array
    for(int num=0;num<input.size();num++)
    {
      if(input[num]>0) countPositive++;     //if value in array >0, add counter
      else if(input[num]<0) sumNegative += input[num];  //if value in array <0, create a subtotal
    }//loop ends here
    return {countPositive,sumNegative}; //return both values to main() or calling function
}//end of function

//main() starts here
int main()
{
 //call the function by sending array of values and collect result as vector back 
 std::vector<int> result = countPositivesSumNegatives({0, 2, 3, 0, 5, 6, 7, 8, 9, 10, -1, -2, -3, -4});

//loop through vector and print all elements in it
 for( int i = 0; i < result.size(); i++ )
    cout << result[i] << endl;
    
 return 0; //end of main()
}
