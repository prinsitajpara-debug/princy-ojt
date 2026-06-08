from fastapi import FastAPI, BackgroundTasks

app = FastAPI()


def send_email(email: str):
    print(f"Sending email to {email}")


@app.post("/notify")
def notify(
    email: str,
    background_tasks: BackgroundTasks
):
    background_tasks.add_task(
        send_email,
        email
    )

    return {
        "message": "Email scheduled successfully"
    }