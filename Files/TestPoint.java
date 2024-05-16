package tester;
import day3practice1.Point;
import java.util.Scanner;
public class TestPoint 
{
	public static void main(String[] args) 
	{
		Scanner qwe = new Scanner(System.in);
		System.out.println("enter value of x & y: ");
		int p = qwe.nextInt();
		int q = qwe.nextInt();
		Point pointobj1 = new Point();
		pointobj1.showPoint();
		Point pointobj2 = new Point(4,3);
		pointobj2.showPoint();
		Point pointobj3 = new Point();
		pointobj3.assignPoint(p, q);
		pointobj3.showPoint();
		qwe.close();
	}
}