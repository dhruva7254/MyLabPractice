package com.bank;
public class Account 
{
	private int accountId;
	private String name;
	private String email;
	private double balance;
	public Account()
	{
		accountId = 101;
		name = "ght";
		email = "ght@gmail.com";
		balance = 24000;
	}
	public Account(int accountId, String name, String email, double balance)
	{
		super();
		this.accountId = accountId;
		this.name = name;
		this.email = email;
		this.balance = balance;
	}
	public void showInfo()
	{
		System.out.println("location of object: "+this.hashCode());
		System.out.println(accountId+"   "+name+"   "+email+"   "+balance);
	}
	public int getAccountId() 
	{
		return accountId;
	}
	public void setAccountId(int accountId) 
	{
		this.accountId = accountId;
	}
	public String getName() 
	{
		return name;
	}
	public void setName(String name) 
	{
		this.name = name;
	}
	public String getEmail() 
	{
		return email;
	}
	public void setEmail(String email) 
	{
		this.email = email;
	}
	public double getBalance() 
	{
		return balance;
	}
	public void setBalance(double balance) 
	{
		this.balance = balance;
	}
	public void deposit(double amount)
	{
		System.out.println("old balance: "+this.balance);
		this.balance += amount;
		System.out.println("new balance after deposit: "+this.balance);
	}
	public void withdraw(double amount)
	{
		System.out.println("old balance: "+this.balance);
		this.balance -= amount;
		System.out.println("new balance after withdraw: "+this.balance);
	}
	public void moneyTransfer(Account reciever, double amount)
	{
		System.out.println("Sender name: "+this.getName());
		System.out.println("Reciever name: "+reciever.getName());
		System.out.println("Sender old balance: "+this.getBalance());
		System.out.println("Reciever old balance: "+reciever.getBalance());
		this.balance -= amount;
		reciever.balance += amount;
		System.out.println("Sender balance after money transfer: "+this.getBalance());
		System.out.println("Reciever balance after money recieved: "+reciever.getBalance());
	}
	
}