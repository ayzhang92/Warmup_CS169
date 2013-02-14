class TestapiController < ApplicationController
  def resetFixture
    User.delete_all()
    render :json => {:errCode => 1}
  end

  def unitTests
    # do stuff
  end
end
