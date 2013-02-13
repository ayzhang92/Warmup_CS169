class UsersController < ApplicationController
  def login
    @username = params[:user]
    @password = params[:password]
    @user = User.find_by_user(@username)
    if @user.nil?
      render :json => {:errCode => -1}
    elsif @password == @user.password
      @user.update_attribute(:count, @user.count + 1)
      render :json => {:errCode => 1, :count => @user.count}
    else
      render :json => {:errCode => -1}
    end
  end

  def add
    @username = params[:user]
    @password = params[:password]
    if User.find_by_user(@username).nil?
      if @username.blank? || @username.length > 128
        render :json => {:errCode => -3}
      elsif @password.length > 128
        render :json => {:errCode => -4}
      else
        @user = User.create(user: @username, password: @password, count: 1)
        render :json => {:errCode => 1, :count => @user.count}
      end
    else
      render :json => {:errCode => -2}
    end
  end


end
