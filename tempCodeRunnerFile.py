if graph_cand == 0:
    try:
      graph_label = Text(Point(320, 231), config[config_linha][0][0]).draw(win)
      draws.append(graph_label)
      print(graph_label)
    except:
      continue