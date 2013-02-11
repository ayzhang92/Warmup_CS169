class User < ActiveRecord::Base
  attr_accessible :count, :password, :user

  validates(:user, :presence => true, :length => {:maximum => 128},
            :message => "The user name should be non-empty and at most 128 characters long. Please try again." )
  validates(:password, :length => {:maximum => 128,
                                   :message => "The password should be at most 128 characters long. Please try again." })

  # add login and add functions in here, and resetFixture
end
