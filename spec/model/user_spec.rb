# spec/models/user_spec.rb
require 'spec_helper'

describe User do

  before { @user = User.new(user: 'albus', password: 'dumbledore') }

  subject { @user }

  it { should respond_to(:user) }  # 1
  it { should respond_to(:password) }  # 2
  it { should respond_to(:count) }  # 3
  it { should be_valid }  # 4

  # 5
  describe 'when user is not present' do
    before { @user.user = '   ' }
    it { should_not be_valid }
  end

  # 6
  describe 'when password is blank' do
    before { @user.password = '   ' }
    it { should be_valid }
  end

  # 7
  describe 'when user is too long' do
    before { @user.user = 'a' * 129 }
    it { should_not be_valid }
  end

  # 8
  describe 'when password is too long' do
    before { @user.password = 'z' * 129 }
    it { should_not be_valid }
  end

  # 9
  describe 'when username is already taken' do
    before do
      user_with_same_username = @user.dup
      user_with_same_username.user = @user.user
      user_with_same_username.save
    end

    it { should_not be_valid }
  end

  # 10
  describe 'increment count on login' do
    before { @user.save }
    it { should be_valid }
  end
end
