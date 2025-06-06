chorme.runtime.onInstalled.addListener(() => {
    const port = chrome.runtime.connectNative("my.host.python");

    port.postMessage({ action: "Convert", img: ""});

    port.onMessage.addListener((response) => {
        console.log("Resposta do Python:", response);
    });

    port.onDisconnect.addListener(() => {
        console.error("Conexão Encerrada!");
    });
});