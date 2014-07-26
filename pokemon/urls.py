from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pokemon.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'match_game.views.home', name='home'),
    url(r'^all_pokemon/$', 'match_game.views.all_pokemon', name='all_pokemon'),
    url(r'^new_pokemon/$', 'match_game.views.new_pokemon', name='new_pokemon'),
    url(r'^dump_pokemon/$', 'match_game.views.all_pokemon', name='all_pokemon'),
    url(r'^serial_pokemon/$', 'match_game.views.serial_pokemon', name='serial_pokemon'),
    url(r'^pokemon_info/(?P<pokemon_id>\w+)/$', 'match_game.views.pokemon_info', name='pokemon_info'),
    url(r'^pokemon_team_info/(?P<team_id>\w+)/$', 'match_game.views.pokemon_team_info', name='pokemon_team_info'),



)
