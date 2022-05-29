# text_game_engine

this is an experimental text game engine for building text based rpg adventures easily.

the core concept is it represents a story as a graph where the nodes are 'story points' and edges are actions (functions) that act on the player.

currently its really rough - and in testing.

(so not 'production ready')


## what's missing:
    --combat system
    --various details.
    --better navigation system.

## what's here:
    -- a small example game (unfinished and just a few nodes)
       -- showcasing some of the logic building possible building a story this way.
       
       
       
## where its going:
    -- what this should be eventually is a fully fledged game engine for text based adventures.
    -- a library of 'standard items and functions' that are easily useable and composable with 'action functions' stored on edges.
    -- probably a major clean up translating the logic from my head to real human logic we can all agree on :)


## details

    -- A story node is just a bit of text with an id.
    -- A story edge has a parent and a child.
    -- when looking for visibile edges from the current story node - each edge is checked to see if the parent matches the story node
        --in addition to matching it also has to pass the (is_hidden) check (which could be any condition)
    -- navigation is done mostly though numbers.
    -- tests are still being written :)
