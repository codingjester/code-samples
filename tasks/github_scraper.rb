require 'nokogiri'
require 'mechanize'

#This was a scraper I wrote in an hour or so
#that I was going to use for some githacking stuff
#eventually, we figured out a better way to do some
#data pulling and went that route.
#This is cool though. Love nokogiri!


class GitHubScraper
    def initialize depth=1
        @depth = depth
        @cur_depth = 0
        @browser = Mechanize.new
    end
    
    
    def get_github_info username 
        page = get_page(username)
        unless page.nil?
            page = Nokogiri::HTML page.body
            #Pull out the info that we want.
            repos = get_repositories page
            name = get_name page
            address = get_location page
            followers = get_followers username
            following = get_following username
            watched_repos = get_watched_repos username
            
            #TODO Build an object that we can use to access info easily
            puts "#{username} has #{repos.size} repositories"
            puts "Real Name: #{name}"
            puts "Lives in: #{address}"
            puts "He has #{followers.size} followers and is following #{following.size} people"

        else
            nil
        end
    end

    def get_repositories page
        repo_node = page.xpath('//ul[@class="repositories"]')
        #Figure out how to reject if it has a class
        repo = repo_node.css('li.public').collect{ |node| [node.xpath('h3/a').text, node.css('ul.repo-stats li')[0].text] }
    end

    def get_watched_repos user
        page = self.get_page(user, 'following')
        unless page.nil?
            page = Nokogiri::HTML page.body
            watched_repos = page.css('ul.repo_list li').collect{ |li| "#{li.css('a span.owner').text}/#{li.css('a span.repo').text}"  }
        end
    end

    def get_following user
        page = self.get_page(user, 'following')
        unless page.nil?
            page = Nokogiri::HTML page.body
            following = page.css('ul.members li').collect{ |li| li.css('a')[1].text }
        end
    end
    
    def get_followers user
        page = self.get_page(user, 'followers')
        unless page.nil?
            page = Nokogiri::HTML page.body
            #pull out the usernames of the followers
            followers = page.css('ul.members li').collect{ |li| li.css('a')[1].text }
        end
    end

    def get_page(user, route=nil)
        begin
            unless route.nil?
                page = @browser.get("http://github.com/#{user}/#{route}")
            else
                page = @browser.get("http://github.com/#{user}")
            end
        rescue Mechanize::ResponseCodeError
            nil
        end
    end

    def get_name page
        page.css("dd.fn").text
    end
    
    def get_location page
        page.css("dd.adr").text
    end
end

x = GitHubScraper.new
puts x.get_github_info('adsfgadfedkfag93921')
puts x.get_github_info('codingjester')

