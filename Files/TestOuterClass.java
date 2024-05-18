package com.may18.tester;
import com.may18.coder.OuterClass;
public class TestOuterClass 
{
	public static void main(String[] args) 
	{
		OuterClass obj1 = new OuterClass(12,"qaz");
		//obj1.setInnerObj(23);
		OuterClass obj2 = new OuterClass(12,"qaz");
		System.out.println(obj1.equals(obj2));
	}
}
