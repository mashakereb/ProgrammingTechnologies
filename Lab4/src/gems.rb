module Gems

  class Preciousness
    PRECIOUS = 'precious'
    SEMIPRECIOUS = 'semiprecious'
  end

  class VisualParameters
    attr_accessor :color, :transparency, :faces_number

    def to_s
      "color: #{@color}, transparency: #{@transparency}, faces number: #{@faces_number}"
    end
  end

  class Gem
    attr_accessor :id, :name, :origin, :visual_parameters, :preciousness, :value

    def initialize
      @visual_parameters = VisualParameters.new
    end

    def to_s
      "id: #{@id}, name: #{@name}, origin: #{@origin}, value: #{@value}," +
              "preciousness: #{@preciousness}, visual parameters: [#{@visual_parameters}]"
    end
  end
end