API URL: https://api.github.com/repos/rails/rails/events?per_page=100

# Input format (Event List)
```
[
    {
        id: "3219029661",
        type: "WatchEvent",
        actor: {
            id: 6626956,
            login: "HeshamAbdalla",
            gravatar_id: "",
            url: "https://api.github.com/users/HeshamAbdalla",
            avatar_url: "https://avatars.githubusercontent.com/u/6626956?"
        }
    }
]
```

# Output format (User List)
```
[
    {
        login: "rafaelfranca",
        events: {
            TotalEvent: 19,
            IssueCommentEvent: 10,
            PullRequestEvent: 2,
            IssuesEvent: 2,
            PushEvent: 1,
            PullRequestReviewCommentEvent: 4
        }
    }
]
```
TotalEvent는 모든 이벤트 숫자를 더한 값

# Parameter
## sort : 주어진 이벤트가 많은 유저 순으로 정렬
default값은 TotalEvent (전체 이벤트 수)
api/github?sort=TotalEvent

1. 각 유저별로 전체 이벤트 갯수
2. 각 유저별로 각 이벤트 갯수
3. 정렬