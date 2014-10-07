require 'rspec'
require_relative '../lib/fakultet'


describe 'fakultet.rb' do



  it 'should take an number as  argument' do
    expect { fakultet() }.to raise_error ArgumentError
    expect { fakultet(number:13)}.not_to raise_error
  end

  it 'should return the correct factorial for numbers between 0 to 100' do
    (0..100).each do |nr|
      expect( fakultet(number:nr) ).to eq  (1..nr).inject(:*) || 1

    end
  end



end
