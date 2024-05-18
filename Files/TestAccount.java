package com.may18.tester;
import com.may18.coder.Account;
import java.util.Scanner;
public class TestAccount 
{
	public static void main(String[] args) 
	{
		Scanner qwe = new Scanner(System.in);
		Account obj1 = new Account();
		System.out.println("Enter ActId, Name, Balance: ");
		Account obj2 = new Account(qwe.nextInt(),qwe.next(),qwe.nextDouble());
		System.out.println("Do you want to apply for Locker (Yes/No): ");
		String qaz = qwe.next();
		if(qaz.toLowerCase().equals("yes"))
		{
			System.out.println("Enter number of Years: ");
			int wsx = qwe.nextInt();
			obj2.applyForLocker(wsx);
		}
		else
		{
			System.out.println("No locker");
		}
		System.out.println(obj2);
		qwe.close();
	}
}
