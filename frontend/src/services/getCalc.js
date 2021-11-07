const getCalcService = async ({ baseO, input, baseC }) => {
  const url = `http://127.0.0.1:5000/calc`

  const settings = {
    method: 'POST',
    body: JSON.stringify({ baseO, input, baseC }),
    headers: new Headers({
      'Content-Type': 'application/json',
    }),
  }

  try {
    const res = await fetch(`${url}`, settings)
    const dataUser = await res.json()
    if (await res) {
      if ((await res.status) !== 200) return [dataUser.results, false]
      else return [dataUser.results, true]
    } else return ['Falló el procesamiento de la solicitud', false]
  } catch (error) {
    console.error(error)
    return [error, false]
  }
}

export default getCalcService
