require_relative 'GemSAXParser'
require_relative 'GemsDOMParser'
require 'nokogiri'


puts 'Validation step'

xsd = Nokogiri::XML::Schema(File.read('../xml/Gems.xsd'))
doc = Nokogiri::XML(File.read('../xml/gems2.xml'))

errors = xsd.validate(doc)
if errors.length > 0
  errors.each do |error|
    puts error.message
  end
else
puts 'The file is valid '
end



puts 'SAX parser'
handler = GemsTokenizer.new
parser = XML::SAX::Parser.new(handler)
parser.parse_file('../xml/Gems.xml')

puts handler.gems

puts 'DOM parser'
parser = GemDomParser.new(Nokogiri::XML(open("../xml/Gems.xml")))
parser.parse
gems = parser.gems
puts gems

puts 'Sorted by value'
puts gems.sort_by{|gem| gem.value}