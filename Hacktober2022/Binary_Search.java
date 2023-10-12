import java.util.*;
public class Main
{
    int binary_search(int a[], int n, int k)
    {
        int mid=0,l=0,h=n-1,ans=0;
        while(l<=h)
        {
            mid=(h+l)/2;
            if(a[mid]==k)
            {
                return mid+1;
            }
            else if(k>a[mid])
                l=mid+1;
            else
                h=mid-1;
        }
        return -1;
    }
     public static void main(String[] args)
    {
        int n;
        Scanner sc=new Scanner(System.in);
        n=sc.nextInt();
        int a[]= new int [n];
        for(int i=0;i<n;i++)
        {
            a[i]=sc.nextInt();
        }
        int k=sc.nextInt();
        Main obj=new Main();
        int ans=obj.binary_search(a,n,k);
        if(ans<0)
            System.out.println("Not Found!");
        else
            System.out.println("Fount At "+ans);
    }
}
