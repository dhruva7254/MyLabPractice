package com.bank;
public class Product 
{
	private int  prdId;
	private String name;
	private double price;
	private Date mDate;
	public Product()
	{
		prdId=101;
		name="xyz";
		price=100;
		mDate=new Date();	
	}
	public Product(int prdId,String name,double price,Date mDate)
	{
		this.prdId=prdId;
		this.name=name;
		this.price=price;
		this.mDate=mDate;				
	}
	public void print()
	 {  
		 System.out.println("PrdId="+this.prdId);
		 System.out.println("Name="+this.name);
		 System.out.println("Price="+this.price);
		 System.out.println("mDate="+this.mDate);
	 }
	public String toString()
	{
		return "PrdId:"+prdId+" Name "+name+"  Price "+price+"  mDate:"+mDate;	
	}
}