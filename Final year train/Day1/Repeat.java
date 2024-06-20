import java.util.*;
// i/p=aaabbaaaaddd   o/p=a3b2a4d3
class Repeat{
    public static void main(String args[])
    {
        Scanner sc=new Scanner(System.in);
        String st=sc.next();
        int n=st.length();
        int c=1;
        for(int i=0;i<n;i++)
        {
            if(i+1<n && st.charAt(i)==st.charAt(i+1))
            {
                c=c+1;
            }
            else
            {
                System.out.print(st.charAt(i)+""+c);
                c=1;
            }
        }
    }
}
