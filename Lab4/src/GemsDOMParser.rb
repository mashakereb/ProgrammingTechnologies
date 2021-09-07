require "nokogiri"
require_relative 'gems'


class GemDomParser
  def initialize(doc)
    @doc = doc
    @gems = Array.new
  end

  def parse
    @doc.search('gem').each do |gem|
      n_gem = Gems::Gem.new
      n_gem.value = gem.at('Value').text.to_f
      n_gem.name = gem.at('Name').text
      n_gem.origin = gem.at('Origin').text
      n_gem.preciousness = gem.at('Preciousness').text
      n_gem.id = gem['id']# add id
      visual_parameters = gem.at('VisualParameters')

      n_gem.visual_parameters.transparency = visual_parameters.at('Transparency').text.to_i
      n_gem.visual_parameters.color = visual_parameters.at('Color').text
      n_gem.visual_parameters.faces_number = visual_parameters.at('FacesNumber').text.to_i

      @gems.push(n_gem)
    end
  end

  def gems
    @gems
  end
end