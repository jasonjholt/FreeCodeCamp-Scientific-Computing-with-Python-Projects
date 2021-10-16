def add_time(start, duration, day=False):
  days_in = {"monday":0, "tuesday":1,"wednesday":2,"thursday":3, "friday":4, "saturday":5, "sunday":6}

  days_out = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

  d = duration.split(":")
  dur_hours = int(d[0])
  dur_min = int(d[1])

  s = start.split(" ")
  am_or_pm = s[1]
  start_time = s[0]
  split_time = start_time.split(":")
  start_hours = int(split_time[0])
  start_minutes = int(split_time[1])

  time_flips = {"AM":"PM", "PM":"AM"}
  # count the flips
  # even number, stays the same
  # odd, use the dictionary

  days_elapsed = dur_hours//24

  end_min = start_minutes + dur_min
  if end_min >= 60:
    start_hours += 1
    end_min = end_min%60


  if (start_hours + dur_hours)%12 == 0:
    end_hours = 12
  elif (start_hours + dur_hours)%12 != 0:
    end_hours = (start_hours + dur_hours)%12
  
  
  if am_or_pm == "PM" and start_hours + (dur_hours%12) >= 12:
    days_elapsed += 1


  flips = (start_hours + dur_hours)//12
  if flips%2 != 0:
    am_or_pm = time_flips[am_or_pm]
  
  new_time = str(end_hours) + ":" + str(end_min).zfill(2) + " " + am_or_pm

  if day:
    given_day = day.lower()
    index = (int(days_in[given_day]) + days_elapsed) % 7
    new_day = days_out[index]
    new_time += ", " + new_day
  
  if days_elapsed == 1:
    new_time += " (next day)"
  if days_elapsed > 1:
    new_time += " (" + str(days_elapsed) + " days later)"


  return new_time
