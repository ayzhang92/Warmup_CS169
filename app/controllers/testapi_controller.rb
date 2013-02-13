class TestapiController < ApplicationController
  # add resetFixture and unitTests functions here??
  def resetFixture
    User.delete_all()
    render :json => {:errCode => 1}
  end

  def unitTests
    # do stuff
  end
end
