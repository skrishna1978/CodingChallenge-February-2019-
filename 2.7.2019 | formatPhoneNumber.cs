//2.7.2019 - Shashi
//C# program that accepts an integer array and returns a String formatted as a phone number.

public class formatNumber //class starts here
{
  public static string createPhoneNumber(int[] numberArray) //function starts here
  {
      if(numberArray.Length<1 || numberArray.Length>10) //to ensure only 10 digits are processed
        return "Invalid Input";
      else
        return long.Parse(string.Concat(numberArray)).ToString("(000) 000-0000");
    //line above does the following from innermost brackets:
    //parse and join all the numbers together, conver them to string and format them to "(000) 000-0000" format
  }//function ends here
  
   static void Main(string[] args)
    {
        //Single line that both calls the function and prints the returned output
        System.Console.WriteLine(createPhoneNumber(new int[]{1,2,3,4,5,6,7,8,9,0})); //sending an array with the new int[] command
        System.Console.WriteLine(createPhoneNumber(new int[]{9,7,4,3,3,1,2,6,7,2,1})); //checking error condition
        System.Console.WriteLine(createPhoneNumber(new int[]{9,7,4,3,3,7,2,1})); //values between 1 and 9 get padded with leading 0s
        System.Console.WriteLine(createPhoneNumber(new int[]{})); //checking error condition
    }//main() ends here
}//class ends here
