class TestapiController < ApplicationController
  def resetFixture
    User.delete_all()
    render :json => {:errCode => 1}
  end

  def unitTests
    render :json => {:totalTests => 10, :nrFailed => 0, :output => 'stuff'}
  end
end
