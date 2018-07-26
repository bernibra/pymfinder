##############################################################
##############################################################
# USEFUL GLOBAL VARIABLES
##############################################################
##############################################################

STOUFFER_MOTIF_IDS = {12:  'S1',
                      38:  'S2',
                      98:  'S3',
                      36:  'S4',
                      6:   'S5',
                      46:  'D1',
                      108: 'D2',
                      14:  'D3',
                      74:  'D4',
                      102: 'D5',
                      238: 'D6',
                      110: 'D7',
                      78:  'D8',
                      }

#key = (npred,nprey)
STOUFFER_ROLE_IDS = dict(zip([(12, 0, 1),
                              (12, 1, 1),
                              (12, 1, 0),
                              (38, 0, 2),
                              (38, 1, 1),
                              (38, 2, 0),
                              (98, 1, 1),
                              (36, 0, 1),
                              (36, 2, 0),
                              (6, 0, 2),
                              (6, 1, 0),
                              (46, 1, 2),
                              (46, 2, 0),
                              (108, 0, 2),
                              (108, 2, 1),
                              (14, 1, 2),
                              (14, 1, 1),
                              (14, 1, 0),
                              (74, 0, 1),
                              (74, 1, 1),
                              (74, 2, 1),
                              (102, 1, 1),
                              (102, 2, 1),
                              (102, 1, 2),
                              (238, 2, 2),
                              (110, 1, 2),
                              (110, 2, 1),
                              (110, 2, 2),
                              (78, 1, 1),
                              (78, 2, 2),],
                             range(30)
                            )
                        )

#key = size:(motif_id, (npred,nprey))
UNIPARTITE_ROLES = {2:[(2, [(0, 1),
                            (1, 0),
                            ]),
                       (6, [(1, 1),
                            ]),
                       ],

                    3:[(12,  [(0, 1),
                              (1, 1),
                              (1, 0),
                              ]),
                       (38,  [(0, 2),
                              (2, 0),
                              (1, 1),
                              ]),
                       (98,  [(1, 1),
                              ]),
                       (36,  [(0, 1),
                              (2, 0),
                              ]),
                       (6,   [(1, 0),
                              (0, 2),
                              ]),
                       (46,  [(1, 2),
                              (2, 0),
                              ]),
                       (108, [(2, 1),
                              (0, 2),
                              ]),
                       (14,  [(1, 1),
                              (1, 0),
                              (1, 2),
                              ]),
                       (74,  [(2, 1),
                              (0, 1),
                              (1, 1),
                              ]),
                       (102, [(1, 2),
                              (1, 1),
                              (2, 1),
                              ]),
                       (238, [(2, 2),
                              ]),
                       (110, [(1, 2),
                              (2, 2),
                              (2, 1),
                              ]),
                       (78,  [(1, 1),
                              (2, 2),
                              ]),
                       ],
                    }

#key as for positions but with two species (eaten by,eats) ((eater),(eaten)))
UNIPARTITE_LINKS_ROLES = {2:[(2,  [((0,1),(1,0)),]),
                       (6,  [((1,1),(1,1)),]),
                        ],

                    3:[
                       (6,   [((0, 2),(1, 0)), 
                              ]),
                       (12,  [((0, 1),(1, 1)), 
                              ((1, 1),(1, 0)), 
                              ]),
                       (14,  [((1, 2),(1, 1)), 
                              ((1, 2),(1, 0)), 
                              ]),
                       (36,  [((0, 1),(2, 0)), 
                              ]),
                       (38,  [((0, 2),(1, 1)), 
                              ((1, 1),(2, 0)), 
                              ((0, 2),(2, 0)), 
                              ]),
                       (46,  [((1, 2),(2, 0)), 
                              ((1, 2),(1, 2)), 
                              ]),
                       (74,  [((0, 1),(2, 1)), 
                              ((1, 1),(2, 1)), 
                              ]),
                       (78,  [((1, 1),(2, 2)), 
                              ]),
                       (98,  [((1, 1),(1, 1)), 
                              ]),
                       (102, [((1, 1),(2, 1)), 
                              ((1, 2),(2, 1)), 
                              ((1, 2),(1, 1)), 
                              ]),
                       (108, [((0, 2),(2, 1)), 
                              ((2, 1),(2, 1)), 
                              ]),
                       (110, [((1, 2),(2, 1)), 
                              ((1, 2),(2, 2)), 
                              ((2, 2),(2, 1)), 
                              ]),
                       (238, [((2, 2),(2, 2)), 
                              ]),
                       ],
                    }

#key = size:(motif_id, (npred,nprey,(degrees of preds, degrees of prey)))
BIPARTITE_ROLES = {2:[(2, [(0, 1),
                           (1, 0),
                           ]),
                      ],

                   3:[(36, [(0, 1),
                            (2, 0),
                            ]),
                      (6,  [(0, 2),
                            (1, 0),
                            ]),
                      ],

                   4:[(2184, [(0, 1),
                              (3, 0),
                              ]),
                      (14,   [(0, 3),
                              (1, 0),
                              ]),
                      (76,   [(0, 1),
                              (2, 0),
                              (0, 2),
                              (1, 0),
                              ]),
                      (204,  [(2, 0),
                              (0, 2),
                              ]),
                      ],

                   5:[(541200, [(0, 1),
                                (4, 0),
                                ]),
                      (30,     [(0, 4),
                                (1, 0),
                                ]),
                      (8728,   [(0, 1),
                                (0, 2),
                                (2, 0),
                                ]),
                      (404,    [(0, 2),
                                (1, 0),
                                (2, 0),
                                ]),
                      (8472,   [(0, 2),
                                (0, 1),
                                (1, 0),
                                (3, 0),
                                ]),
                      (156,    [(0, 3),
                                (0, 1),
                                (1, 0),
                                (2, 0),
                                ]),
                      (8984,   [(0, 2),
                                (0, 1),
                                (2, 0),
                                (3, 0),
                                ]),
                      (412,    [(0, 3),
                                (0, 2),
                                (1, 0),
                                (2, 0),
                                ]),
                      (25368,  [(0, 2),
                                (3, 0),
                                ]),
                      (924,    [(0, 3),
                                (2, 0),
                                ]),
                      ],
                   
                   6:[(545392672, [(0, 1),
                                   (5, 0),
                                   ]),
                      (62,        [(0, 5),
                                   (1, 0),
                                   ]),
                      (4261936,   [(0, 1, (2,)),
                                   (0, 2),
                                   (0, 1, (3,)),
                                   (2, 0),
                                   (3, 0),
                                   ]),
                      (820,       [(0, 2),
                                   (0, 3),
                                   (1, 0, (2,)),
                                   (2, 0),
                                   (1, 0, (3,)),
                                   ]),
                      (4260912,   [(0, 2),
                                   (0, 1),
                                   (1, 0),
                                   (4, 0),
                                   ]),
                      (316,       [(0, 1),
                                   (0, 4),
                                   (2, 0),
                                   (1, 0),
                                   ]),
                      (4262960,   [(0, 1),
                                   (0, 2),
                                   (4, 0),
                                   (2, 0),
                                   ]),
                      (828,       [(0, 2),
                                   (0, 4),
                                   (2, 0),
                                   (1, 0),
                                   ]),
                      (4328496,   [(0, 1),
                                   (0, 2),
                                   (3, 0),
                                   ]),
                      (1836,      [(0, 3),
                                   (1, 0),
                                   (2, 0),
                                   ]),
                      (4394032,   [(0, 2),
                                   (0, 1),
                                   (3, 0),
                                   (4, 0),
                                   ]),
                      (1852,      [(0, 3),
                                   (0, 4),
                                   (2, 0),
                                   (1, 0),
                                   ]),
                      (12782640,  [(0, 2),
                                   (4, 0),
                                   ]),
                      (3900,      [(0, 4),
                                   (2, 0),
                                   ]),
                      (34352,     [(0, 2, (1,2,)),
                                   (0, 2, (2,2,)),
                                   (0, 1),
                                   (1, 0),
                                   (2, 0, (2,2,)),
                                   (2, 0, (1,2,)),
                                   ]),
                      (33848,     [(0, 1),
                                   (0, 3),
                                   (2, 0),
                                   (1, 0),
                                   ]),
                      (34344,     [(0, 2),
                                   (0, 1),
                                   (1, 0),
                                   (3, 0),
                                   ]),
                      (33336,     [(0, 1),
                                   (0, 3),
                                   (3, 0),
                                   (1, 0),
                                   ]),
                      (99880,     [(0, 2, (1,3,)),
                                   (0, 2, (2,3,)),
                                   (1, 0),
                                   (3, 0),
                                   (2, 0),
                                   ]),
                      (34360,     [(0, 1),
                                   (0, 2),
                                   (0, 3),
                                   (3, 0),
                                   (2, 0),
                                   (1, 0),
                                   ]),
                      (35896,     [(0, 2),
                                   (0, 3),
                                   (0, 1),
                                   (2, 0, (2,3,)),
                                   (2, 0, (1,3,)),
                                   ]),
                      (100912,    [(0, 2),
                                   (2, 0),
                                   ]),
                      (36408,     [(0, 1),
                                   (0, 3),
                                   (3, 0),
                                   (2, 0),
                                   ]),
                      (99896,     [(0, 3),
                                   (0, 2),
                                   (1, 0),
                                   (3, 0),
                                   ]),
                      (100920,    [(0, 2),
                                   (0, 3),
                                   (2, 0),
                                   (3, 0),
                                   ]),
                      (101944,    [(0, 3),
                                   (0, 2),
                                   (2, 0),
                                   (3, 0),
                                   ]),
                      (233016,    [(0, 3),
                                   (3, 0),
                                   ]),
                      ],
                   }


BIPARTITE_LINKS_ROLES = {2:[(2,  [((0,1),(1,0)),])],
    3:[(36, [((0,1),(2,0)),]),
      (6, [((0,2),(1,0)),]),
      ],
    4:[ # (pred, prey) ((npred,nprey))
        (14,   [((0, 3),(1, 0)),]), # One link in the fan with 1 animal, 3 plants
        (76,   [((0,1),(2,0)),
               ((0,2),(2,0)),
               ((0,2),(1,0)),]), # 3 links in the N
        (204,  [((0,2),(2,0)),]), # One link in the X
        (2184, [((0, 1),(3, 0)),]), # One link in the fan with 3 animals, 1 plant
        ],
    5:[
        (30,   [((0, 4),(1, 0)),]),
        (156,  [((0, 1),(2, 0)),
                ((0, 3),(2, 0)),
                ((0, 3),(1, 0)),]),
        (404,  [((0, 2),(1, 0)),
                ((0, 2),(2, 0)),]),
        (412,  [((0, 2),(2, 0)),
                ((0, 3),(2, 0)),
                ((0, 3),(1, 0)),]),
        (924,  [((0, 3),(2, 0)),]),
        (8472, [((0, 1),(3, 0)),
                ((0, 2),(3, 0)),
                ((0, 2),(1, 0)),]),
        (8728, [((0, 1),(2, 0)),
                ((0, 2),(2, 0)),]),
        (8984, [((0, 1),(3, 0)),
                ((0, 2),(3, 0)),
                ((0, 2),(2, 0)),]),
        (25368, [((0, 2),(3, 0)),]),
      (541200, [((0, 1),(4, 0)),]),
        ],
    6:[ (62,        [((0, 5),(1, 0)),]),
        (316,       [((0, 1),(2, 0)),
                     ((0, 4),(2, 0)),
                     ((0, 4),(1, 0)),]),
        (820,       [((1, 0), (0, 2)),
                     ((1, 0), (0, 3)),
                     ((0, 2),(2, 0)),
                     ((0, 3),(2, 0)),
                     ]),
        (828,       [((0, 2),(2, 0)),
                     ((0, 4),(2, 0)),
                     ((0, 4),(1, 0)),]),
        (1836,      [((0, 3),(1, 0)),
                     ((0, 3),(2, 0)),]),
        (1852,      [((0, 3),(2, 0)),
                     ((0, 4),(2, 0)),
                     ((0, 4),(1, 0)),]),
        (3900,      [((0, 4),(2, 0)),]),
        (33336,     [((0, 1),(3, 0)),
                     ((0, 3),(3, 0)),
                     ((0, 3),(1, 0)),]),
        (33848,     [((0, 1),(2, 0)),
                     ((0, 3),(2, 0)),
                     ((0, 3),(1, 0)),]),
        (34344,     [((0, 1),(3, 0)),
                     ((0, 2),(3, 0)),
                     ((0, 2),(1, 0)),]),
        (34352,     [#((2, 0), (0, 2)), # This covers 2 unique roles
                     ((2, 0), (0, 1)),
                     ((1, 0), (0, 2)),
                     ((0, 2, (2,2,)),(2, 0, (1,2,))),
                     ((0, 2, (2,2,)),(2, 0, (2,2,))),
                     ((0, 2,(1,2,)),(2, 0, (2,2,))),
                     ]),
        (34360,     [((0, 1),(3, 0)),
                     ((0, 2),(3, 0)),
                     ((0, 2),(2, 0)),
                     ((0, 3),(3, 0)),
                     ((0, 3),(2, 0)),
                     ((0, 3),(1, 0)),]),
        (35896,     [((2, 0), (0, 1)),
                     ((2, 0), (0, 2)),
                     #((2, 0), (0, 3)), # Also covers 2 unique roles
                     ((0, 3),(2, 0, (1,3,))),
                     ((0, 3),(2, 0, (2,3,))),
                     ]),
        (36408,     [((0, 1),(3, 0)),
                     ((0, 3),(3, 0)),
                     ((0, 3),(2, 0)),]),
        (99880,     [
                     ((0,2), (1,0)),
                     ((0,2), (2,0)),
                     # ((1, 0), (0, 2)),
                     # ((2, 0), (0, 2)),
                     #((3, 0), (0, 2)), # Also covers 2 unique roles
                     ((0, 2, (1,3,)),(3, 0)),
                     ((0, 2, (2,3,)),(3, 0)),
                     ]),
        (99896,     [((0, 2),(3, 0)),
                     ((0, 3),(3, 0)),
                     ((0, 3),(1, 0)),]),
        (100912,    [((0, 2),(2, 0)),]),
        (100920,    [((0, 2),(2, 0)),
                     ((0, 2),(3, 0)),
                     ((0, 3),(2, 0)),
                     ((0, 3),(3, 0)),]),
        (101944,    [((0, 3),(2, 0)),
                     ((0, 3),(3, 0)),
                     ((0, 2),(2, 0)),
                     ((0, 2),(3, 0)),]),
        (233016,    [((0, 3),(3, 0)),]),
        (4260912,   [((0, 2),(1, 0)),
                     ((0, 2),(4, 0)),
                     ((0, 1),(4, 0)),]),
        (4261936,   [((2, 0), (0, 1)),
                     ((3, 0), (0, 1)), 
                     ((0, 2),(2, 0)),
                     ((0, 2),(3, 0)),]),
        (4262960,   [((0, 1),(4, 0)),
                     ((0, 2),(4, 0)),
                     ((0, 2),(2, 0)),]),
        (4328496,   [((0, 1),(3, 0)),
                     ((0, 2),(3, 0)),]),                 
        (4394032,   [((0, 2),(3, 0)),
                     ((0, 2),(4, 0)),
                     ((0, 1),(4, 0)),]),
        (12782640,  [((0, 2),(4, 0)),]),
      (545392672, [((0, 1),(5, 0)),]),
            ],
    }
