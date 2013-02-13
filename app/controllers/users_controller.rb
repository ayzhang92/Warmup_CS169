class UsersController < ApplicationController
  def login
    username = params[:user]
    password = params[:password]
    begin
      @user = User.find_by_user(username)
      if password == user.password
        @user.update_attribute(:count, :count+1)
        render :json => {:errCode => 1, :count => @user.count}
      else
        render :json => {:errCode => -1}
      end
    rescue ActiveRecord::RecordNotFound
      render :json => {:errCode => -1}
    end
  end

  def add
    username = params[:user]
    password = params[:password]
    begin
      @existing = User.find_by_user(username)
      render :json => {errCode => -2}
    rescue ActiveRecord::RecordNotFound
      if username.blank? || username.length > 128
        render :json => {:errCode => -3}
      elsif password.length > 128
        render :json => {:errCode => -4}
      else
        @user = User.create(user: username, password: password, count: 1)
        render :json => {:errCode => 1, :count => @user.count}
      end
    end
  end

end
