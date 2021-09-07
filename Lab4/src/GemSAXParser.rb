require 'rubygems'
require 'nokogiri'
require_relative 'gems'

include Nokogiri

class GemsTokenizer < XML::SAX::Document
  def initialize
    @gems = nil
    @cur_gem = nil

  end

  def gems
    @gems
  end

  def start_element(name, attributes)
    if name == 'gem'
        @cur_gem = Gems::Gem . new
        @cur_gem.id = attributes[0][1]
    end
    @state = name

  end

  def end_element(name)
    if name ==  'gem'
      @gems.push(@cur_gem)
    end

    @state = nil
  end

  def characters(string)
    case @state
      when 'Preciousness'
        @cur_gem.preciousness = string
      when 'Transparency'
        @cur_gem.visual_parameters.transparency = string.to_i
      when 'Name'
        @cur_gem.name = string
      when 'Value'
        @cur_gem.value = string.to_f
      when 'Origin'
        @cur_gem.origin = string
      when 'Color'
       @cur_gem.visual_parameters.color = string
      when 'FacesNumber'
        @cur_gem.visual_parameters.faces_number = string.to_i
    end
  end

  def end_document
    puts 'End of parsing ...'
  end

  def start_document
    puts 'Start parsing the document ...'
    @gems = Array.new
  end
end


